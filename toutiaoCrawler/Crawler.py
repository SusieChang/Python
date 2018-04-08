import requests
import os
from hashlib import md5
from urllib.parse import urlencode
from requests.exceptions import RequestException
from json import JSONDecodeError
from multiprocessing import Pool
import json
import re
import pymongo
import lxml
import random
from bs4 import BeautifulSoup
from config import *

headers = {'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           }

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]
user_agents=[]


def get_user_agents_from_file():
    file_path = 'resource/user_agents.txt'
    print('reading user_agents....')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                user_agents.append(line.strip())
            f.close()
        return user_agents
    return None


def get_page_index(offset, keyword, proxies):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    headers['User-Agent'] = random.choice(user_agents)
    try:
        response = requests.get(url, headers=headers, timeout=5, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
            print('请求索引页出错')
            return None


def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                if item:
                    article_url = item.get('article_url')
                    if article_url:
                        yield article_url
    except JSONDecodeError:
        pass


def get_page_detail(url, proxies):
    headers['User-Agent'] = random.choice(user_agents)
    try:
        response = requests.get(url=url, headers=headers, timeout=20, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
            print('请求详情页出错', url)
            return None


def parse_page_detail(html, url, proxies):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    images_pattern = re.compile('gallery: JSON.parse\((.*?)\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        temp = result.groups(1)
        str1 = "".join(tuple(temp))
        str2 = eval("{}".format(str1))
        data = json.loads(str2)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image, proxies)
            return {
                    'title': title,
                    'url': url,
                    'images': images
                }


def save_to_db(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False


def download_image(url, proxies):
    print('正在下载', url)
    headers['User-Agent'] = random.choice(user_agents)
    try:
        response = requests.get(url=url, headers=headers, timeout=20, proxies=proxies)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
            print('请求图片出错', url)
            return None


def save_image(connect):
    file_path = '{0}/{1}/{2}.{3}'.format('resource/img', KEYWORD, md5(connect).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(connect)
            f.close()


def main(offset):
    get_user_agents_from_file()
    proxy = '118.114.77.47:8080'
    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy
    }

    html = get_page_index(offset, KEYWORD, proxies)
    for url in parse_page_index(html):
        html = get_page_detail(url, proxies)
        if html:
            result = parse_page_detail(html, url, proxies)
            if result:
                save_to_db(result)


if __name__ == '__main__':
    pool = Pool()
    groups = [x*20 for x in range(GROUP_START, GROUP_END+1)]
    pool.map(main, groups)
    pool.close()
    pool.join()

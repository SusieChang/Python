import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
import pymongo
from multiprocessing import Pool


headers = {'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           }

MONGO_URL = '127.0.0.1:27017'
MONGO_DB = 'ProxyPool'
MONGO_TABLE = 'IP4ProxyPool'
client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


def get_page_proxy_content(url):
    try:
        res = requests.get(url, headers=headers, timeout=3)
        response = res.text
        if response:
            return response
    except RequestException:
        print('请求代理地址主页面失败')
        return None


def parse_page_proxy(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')
    for tds in trs[1:]:
        td = tds.find_all('td')
        proxy = str(td[1].contents[0]) + ":" + str(td[2].contents[0])
        if check_proxy(proxy):
            return proxy
    return None


def get_proxys(index):
    url = 'http://www.xicidaili.com/nn/' + str(index)
    content = get_page_proxy_content(url)
    if content:
        proxy = parse_page_proxy(content)
        if proxy:
                proxies = {
                "http": "http://" + proxy,
                "https": "http://" + proxy
                }
                return proxies
    return None


def check_proxy(proxy):
    url = 'http://ip.chinaz.com/getip.aspx'
    try:
        proxyhandler = {
            "http": "http://" + proxy,
            "https": "http://" + proxy
        }
        response = requests.get(url, proxies=proxyhandler, timeout=3)
        if response.status_code == 200 and re.findall('{ip:.*?,address:..*?}', response.text):
            print('valid:', proxy)
            return proxy
    except RequestException:
        pass
    return None


def save_to_proxy_db(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False


def main(index):
    result = get_proxys(index)
    if result:
        save_to_proxy_db(result)


if __name__ == '__main__':
    pool = Pool()
    groups = [x for x in range(1, 6)]
    pool.map(main, groups)
    pool.close()
    pool.join()


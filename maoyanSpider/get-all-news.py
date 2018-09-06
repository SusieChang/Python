import re
import requests
import time
import json
from requests.exceptions import RequestException


def get_page(url):
    try:
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_news_url(html):
    pattern = re.compile('<div.*?news-box.*?<a.*?news-img.*?href="(.*?)".*?</a>', re.S)
    urls = re.findall(pattern, html)
    for url in urls:
        yield 'http://maoyan.com' + url


def parse_news_page(html):
    pattern = re.compile('<div.*?news-title.*?<h1>(.*?)</h1>.*?<div.*?news-subtitle.*?>(.*?)<span.*?</span>(.*?)</div>.*?<div.*?news-content.*?>(.*?)</div>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'newsTitle' : item[0],
            'newsTime' : item[1].strip()[-23:-12],
            'viewCount' : item[2].strip(),
        }


def write_to_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False))


def main(offset):
    main_url = 'http://maoyan.com/news?showTab=2&offset='+ str(offset)
    html = get_page(main_url)
    count = 0
    if html:
        for url in get_news_url(html):
            print(url)
            time.sleep(2)
            content = get_page(url)
            for item in parse_news_page(content):
                print(item)


if __name__ == '__main__':
    main(0)
import requests
import re
import os
import json

def get_home_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_latest_news(html):
    pattern = re.compile('<div.*?latest-news-box.*?<a.*?href="(.*?)".*?src="(.*?)".*?</a>.*?latest-news-title.*?<a.*?title="(.*?)".*?</a>.*?<span.*?images-view-count.*?>(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'imgUrl' : item[1][0:-16],
            'newsLink' : 'http://maoyan.com' + item[0],
            'newsTitle' : item[2],
            'viewCount' : item[3],
        }


def parse_latest_video(html):
    pattern = re.compile('<div.*?latest-video-box.*?<a.*?href="(.*?)".*?data-src="(.*?)".*?<span.*?latest-video-title.*?>(.*?)</span>.*?<span.*?video-play-count.*?>(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'imgUrl' : item[1][0:-16],
            'videoLink' : 'http://maoyan.com' + item[0],
            'newsTitle' : item[2],
            'viewCount' : item[3]
        }


def write_to_file(content, file_path):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    url = 'http://maoyan.com/news'
    html = get_home_page(url)
    if html:
        for item1 in parse_latest_news(html):
            print(item1)
        for item2 in parse_latest_video(html):
            print(item2)


if __name__ == '__main__':
    main()
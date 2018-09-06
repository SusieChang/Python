import re
import requests
import time
import json
from bs4 import BeautifulSoup
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


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    contents = soup.find_all(attrs={'class': 'video-box'})
   # for content in contents:

    #for content in contents:
     #   pattern = re.compile('<img.*?src="(.*?)".*?/>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?<span.*?>(.*?)</span>', re.S)
      #  item = re.findall(pattern, str(content))
       # print(item)


def main():
    url = 'http://maoyan.com/news?showTab=3'
    html = get_page(url)
    if html:
        parse_page(html)


if __name__ == '__main__':
    main()
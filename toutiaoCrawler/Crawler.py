import re
from urllib import request
import json

value = {
    'offset': '0',
    'format':'json',
    'keyword': '古建筑',
    'autoload': 'true',
    'count': '20',
    'cur_tab':'1',
    'from': 'search_tab'
}
data = json.dump(value)

# 获得主页面
def get_page_search():
    req = request.Request('https://www.toutiao.com/',data)
    res = request.urlopen(req)
    print(res.read())

# 获得详情页面
def get_page_detail():

# 获得图片对象
def get_pic_json():

# 解析获得对象
def parse_to_url():

# 保存图片到mangodb
def save_to_db():

# 主函数
def main():

# 入口
if __name__ == __main__:

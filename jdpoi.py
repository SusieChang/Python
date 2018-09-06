#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import re
import pymongo

params = { 
    'province' : '广东',
    'keyword' : '中山大学',
    'city' : '',
    'district' : '',
    'page' : '1',
    'appkey' : '77b95ab8d706104de2c63737eb243f12'
}

def get_all_address(url, totalpage):
    params['page'] = str(index+1)
    response = requests.post( url, params )
    data = response.json()
    poi = data["result"]["result"]
    for item in poi:
        yield item



def main():
    url = 'https://way.jd.com/Bigmap/University'
    response = requests.post( url, params )
    data = response.json()
    totalpage = data["totalPage"]
    for index in range(totalpage):
        for item in get_all_address(url, totalpage):
            save_to_db()


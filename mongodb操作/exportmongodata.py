#coding=utf-8
import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient
import pandas as pd


#连接数据库
client=MongoClient("ds223542.mlab.com", 23542)
db=client.sysu
col=db.jd_address
db.authenticate("sysu","sysu2018")

index = 1
data = col.find()
for item in data:
	print(str(index) + "," +item["name"]+","+item["province"] +","+item["district"] + "," + item["city"]+","+item["address"])
	index=index+1
#coding=utf-8
import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient
import demjson
  
#连接数据库
client = pymongo.MongoClient("mongodb://sysu:sysu2018@cluster0-shard-00-00-gmjko.mongodb.net:27017/admin?ssl=true&replicaSet=cluster0-shard-00-00-gmjko&authSource=admin");
db = client.geokg
col=db.region

data=xlrd.open_workbook("E:/资料/大三下/实训/广府建筑表格/region.xls")
table=data.sheets()[0]
#读取excel第一行数据作为存入mongodb的字段名
rowstag=table.row_values(0)
nrows=table.nrows
ncols=table.ncols
returnData={}

for i in range(1,nrows):
	#将字段名和excel数据存储为字典形式，并转换为json格式
	#returnData[i]=json.dumps(dict(zip(rowstag,table.row_values(i))))
	returnData[i]=json.dumps(dict(zip(rowstag,[table.row_values(i)[0],demjson.decode(table.row_values(i)[1])])))
	#通过编解码还原数据
	returnData[i]=json.loads(returnData[i])
	# print()
	print(returnData[i])
	# col.insert(returnData[i])
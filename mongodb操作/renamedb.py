import requests
from requests.exceptions import RequestException
import pymongo
from lxml import etree
import random
import json
import demjson
import time
from pymongo.errors import PyMongoError
import re

MONGO_URI = 'ds133601.mlab.com:33601'
MONGO_DB = 'sysu_copy'
USERNAME = "sysu"
PASSWORD = "sysu2018"
client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
db.authenticate(USERNAME, PASSWORD)

# db["address"].rename("building")
# db["campus"].update({},{'$unset':{'campusID':""}},multi = True)
# db.campus.update({}, {$rename : {"zoneID" : "belongTo"}}, false, true) 命令行
 db.building.update({}, {$rename : {"campusID" : "belongTo"}}, false, true)
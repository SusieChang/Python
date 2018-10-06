#encoding:utf-8
import pymongo
from bson import ObjectId

MONGO_TABLE = 'address'
MONGO_URI = 'ds113693.mlab.com:13693'
MONGO_DB = 'geokg'
USERNAME = "sysu"
PASSWORD = "sysu2018"

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
db.authenticate(USERNAME, PASSWORD)

db["region"].update({},{'$unset':{'id':""}},multi = True)
db["district"].update({},{'$unset':{'id':""}},multi = True)
db["building"].update({},{'$unset':{'id':""}},multi = True)
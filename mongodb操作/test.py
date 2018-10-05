#encoding:utf-8
import pymongo
from bson import ObjectId

MONGO_URI = 'ds117691.mlab.com:17691'
MONGO_DB = 'maoyanmovie'
USERNAME = "heygrandpa"
PASSWORD = "SYSU2018"

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
db.authenticate(USERNAME, PASSWORD)

result=db["maoyanmovie"].find({},{})
names = []
prices = []
for item in result:
	names.append(item["movie_name"])
	prices.append(item["movie_total_price"])

i = 0
for name in names:
	db.star_movie.update({"movie_name": name},{"$set": {"movie_total_price.$": prices[i]}}, multi=True)
	i = i + 1 
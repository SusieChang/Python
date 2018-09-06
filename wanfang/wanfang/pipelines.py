# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem


def removeUselessValue(array):
    for a in array:
        if a == '' or a == 0 or a == '[1]' or a == '[2]' or a == '[3]' or a == '[4]':
            array.remove(a)


class WanfangPipeline(object):
    def process_item(self, item, spider):
        if item['key_word']:
            item['key_word'] = [i for i in item['key_word'] if i != '']
        if item['c_author']:
            item['c_author'] = [i for i in item['c_author'] if (i != '' and i != '[1]' and i != '[2]' and i != '[3]' and i != '[4]')]
        if item['e_author']:
            item['e_author'] = [i for i in item['e_author'] if i != '']
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        if self.db[name].find_one({'url': item['url']}):
            self.db[name].update({'url': item['url']},{'$set': dict(item)})
        else:
            self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

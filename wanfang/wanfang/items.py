# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WanfangItem(scrapy.Item):
    url = scrapy.Field()
    c_title = scrapy.Field()
    e_title = scrapy.Field()
    doi = scrapy.Field()
    c_author = scrapy.Field()
    e_author = scrapy.Field()
    c_abstract = scrapy.Field()
    e_abstract = scrapy.Field()
    key_word = scrapy.Field()

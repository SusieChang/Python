# -*- coding: utf-8 -*-

# Scrapy settings for qunaer project
BOT_NAME = 'qunaer'

SPIDER_MODULES = ['qunaer.spiders']
NEWSPIDER_MODULE = 'qunaer.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3

#SPIDER_MIDDLEWARES = {
#    'qunaer.middlewares.QunaerSpiderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'qunaer.middlewares.RandomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
	'qunaer.pipelines.MongoPipeline': 400,
   'qunaer.pipelines.QunaerPipeline': 300,
}

MONGO_URI='mongodb://sysu:sysu2018@ds223542.mlab.com:23542'
MONGO_DB='sysu'
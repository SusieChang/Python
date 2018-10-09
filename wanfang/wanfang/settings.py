# -*- coding: utf-8 -*-
BOT_NAME = 'wanfang'

SPIDER_MODULES = ['wanfang.spiders']
NEWSPIDER_MODULE = 'wanfang.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 32

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'wanfang.middlewares.RandomUserAgentMiddleware': 401,
    'wanfang.middlewares.ABProxyMiddleware': 1,
}

# Configure item pipelines
ITEM_PIPELINES = {
   'wanfang.pipelines.MongoPipeline': 400,
    'wanfang.pipelines.WanfangPipeline': 300
}

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

KEY_WORD = '岭南 传统建筑'
MAX_PAGE = 3

MONGO_URI='mongodb://47.106.173.16:27017'
MONGO_DB='wanfang'


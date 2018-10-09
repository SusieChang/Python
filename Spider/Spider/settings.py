# -*- coding: utf-8 -*-

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    #'Spider.middlewares.SpiderDownloaderMiddleware': 543,
    'Spider.middlewares.RandomUserAgentMiddleware': 401,
    'Spider.middlewares.ABProxyMiddleware': 1,
}

# Configure item pipelines
# ITEM_PIPELINES = {
#     'Spider.pipelines.MongoPipeline': 400,
#     'Spider.pipelines.WanfangPipeline': 300,
# }
#
# MONGO_URI='mongodb://47.106.173.16:27017'
# MONGO_DB='Spider'
#
# KEY_WORD = '岭南 传统建筑'
# MAX_PAGE = 30






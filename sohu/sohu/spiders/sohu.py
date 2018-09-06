import scrapy
from sohu.settings import KEY_WORD
from sohu.settings import MAX_PAGE
from scrapy.http import Request
from sohu.items import SoHuItem


class SoHuSpider(scrapy.Spider):
    def __init__(self):
        self.key_word = KEY_WORD
        self.max_page = MAX_PAGE
        self.base_url = 'https://www.so.com/s?site=sohu.com&rg=1&q='+self.key_word

    name = 'sohu'
    allowed_domains = ['sohu.com']

    def start_requests(self):
        for index in range(self.max_page):
            start_url = self.base_url + '&pn=' + str(index+1)
            yield Request(url=start_url, callback=self.parse,meta={'dont_redirect': False,'handle_httpstatus_list': [302]})

    def parse(self, response):
        url_list = response.xpath('//div[@id="main"]/ul[@class="result"]/li[@class="res-list"]/h3/a/@data-url').extract()
        for url in url_list:
            yield Request(url=url, callback=self.parse_item, meta={'refer': url})

    def parse_item(self, response):
        item = SoHuItem()
        item['url'] = response.meta['refer']
        title = response.xpath('//div[@id="article-container"]/div[@class="left main"]/div[@class="text"]/div[@class="text-title"]/h1/text()').extract()
        article = response.xpath('//article[@id="mp-editor"]/p//text()').extract()
        img = response.xpath('//article[@id="mp-editor"]/p/img/@src').extract()
        print(article)
        item['title'] = ''.join(title).strip()
        item['article'] = ''.join([i for i in article if i != '']).strip()
        item['img'] = img
        yield item

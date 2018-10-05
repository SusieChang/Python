# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import math
from lxml import etree
from qunaer.items import QunaerItem


class QunarSpider(scrapy.Spider):
    name = 'qunar'
    allowed_domains = ['qunar.com']
    keyword = "广东"
    base_url = "http://piao.qunar.com/ticket/list.htm"
    subjects = ["文化古迹"]
    #, "古建筑", "古镇", "遗址", "世界遗产", "故居", "古街", "寺庙"]

    def start_requests(self):
        for subject in self.subjects:
            request_url = self.base_url + "?from=mps_search_suggest&keyword="+self.keyword +"&subject=" + subject
            yield Request(url=request_url, callback=self.parse, meta={'request_url': request_url})

    def parse(self, response):
        count = response.xpath('//div[@id="pager-container"]/@data-total-count').extract_first()
        count = int(count)
        max_page = int(math.ceil(count/15))
        for index in range(1, max_page):
            url = response.meta['request_url'] + "&page="+ str(index)
            yield Request(url=url, callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        search_result = response.xpath('//div[@id="search-list"]/div[@class="sight_item sight_itempos"]').extract()
        for item in search_result:
            selector = etree.HTML(str(item))
            name = selector.xpath('//div[@class="sight_item sight_itempos"]/@data-sight-name')
            districts = selector.xpath('//div[@class="sight_item sight_itempos"]/@data-districts')
            address = selector.xpath('//div[@class="sight_item sight_itempos"]/@data-address')
            qunarItem = QunaerItem()
            qunarItem['name'] = ''.join(name).strip()
            qunarItem['districts'] = ''.join(districts).strip()
            qunarItem['address'] = ''.join(address).strip()
            yield qunarItem


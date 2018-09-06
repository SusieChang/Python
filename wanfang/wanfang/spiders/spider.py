# -*- coding: utf-8 -*-
import scrapy
from wanfang.settings import KEY_WORD
from wanfang.settings import MAX_PAGE
from scrapy.http import Request
from wanfang.items import WanfangItem


class WanfangSpider(scrapy.Spider):
    def __init__(self):
        self.base_url = 'http://s.wanfangdata.com.cn/Paper.aspx?'
        self.key_word =  KEY_WORD
        self.max_page = MAX_PAGE

    name = 'wanfang'
    allowed_domains = ['wanfangdata.com.cn']

    def start_requests(self):
        start_url = self.base_url + 'q=' + self.key_word + '&f=top&p=1'
        yield Request(url=start_url, callback=self.parse)

    def parse(self, response):
        page_link = response.xpath('//div[@class="right"]/div[@class="record-item-list"]/p[@class="pager"]/span[@class="page_link"]/text()').extract()
        max_page = int(page_link[0].split("/")[1])
        for index in range(max_page):
            url = self.base_url + 'q=' + self.key_word + '&f=top&p=' + str(index+1)
            if index < self.max_page :
                yield Request(url=url, callback=self.parse_result, dont_filter=True)

    def parse_result(self, response):
        url_list = response.xpath('//div[@class="record-item-list"]/div[@class="record-item"]/div[@class="left-record"]/div[@class="record-title"]/a[@class="title"]/@href').extract()
        for url in url_list:
            yield Request(url=url, callback=self.parse_info, meta={'refer': url}, dont_filter=True)

    def parse_info(self, response):
        item = WanfangItem()
        baseinfo = response.xpath('//div[@class="fixed-width baseinfo clear"]/div[@class="section-baseinfo"]')
        c_title = baseinfo.xpath('//h1/text()').extract()
        e_title = baseinfo.xpath('//h2/text()').extract()
        abstract = response.xpath('//div[@class="baseinfo-feild abstract"]')
        c_abstract = abstract.xpath('//div[@class="row clear zh"]/div[@class="text"]/text()').extract()
        e_abstract = abstract.xpath('//div[@class="row clear fl"]/div[@class="text"]/text()').extract()
        content = response.xpath('//div[@class="fixed-width-wrap fixed-width-wrap-feild"]/div[@class="fixed-width baseinfo-feild"]')
        doi = content.xpath('//span[contains(text(),"doi")]/following-sibling::*[1]/a/text()').extract()
        c_author = content.xpath('//span[contains(text(),"作者：")]/following-sibling::*[1]/a/text()').extract()
        e_author = content.xpath('//span[contains(text(),"Author")]/following-sibling::*[1]//text()').extract()
        key_word = content.xpath('//div[@class="row row-keyword"]/span[@class="text"]//text()').extract()

        item['url'] = response.meta['refer']
        item['c_title'] = ''.join(c_title).strip()
        item['e_title'] = ''.join(e_title).strip()
        item['c_abstract'] = ''.join(c_abstract).strip()
        item['e_abstract'] = ''.join(e_abstract).strip()
        item['doi'] = ''.join(doi).strip()
        item['c_author'] = [''.join(author).strip() for author in c_author]
        item['e_author'] = [''.join(author).strip() for author in e_author]
        item['key_word'] = [''.join(word).strip() for word in key_word]

        yield item






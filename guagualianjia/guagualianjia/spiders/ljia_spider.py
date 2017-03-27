#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'SZ'

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from scrapy.linkextractors import SgmlLinkExtractor
from guagualianjia.items import GuagualianjiaItem

# class LianjiaSpider(scrapy.Spider):


class LianjiaSpider(CrawlSpider):
    name = "lianjiaspider"

    allowed_domains = ['bj.lianjia.com']
    custom_settings = {
        'ROBOTSTXT_OBEY': 'false',
    }
    start_urls = (
        'http://bj.lianjia.com/ershoufang/101101233032.html',
    )
    rules = (
        # Rule(LinkExtractor(allow=('ershoufang/[0-9]*\.html', )),
        #      callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=(
            r'http://bj.lianjia.com/ershoufang/[0-9]*\.html')), callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        self.logger.info(
            'Hi, -------------------------this is an item page! %s', response.url)
        item = GuagualianjiaItem()
        infobase = response.xpath(
            "//body//div[@class='m-content']//div[@class='box-l']//div[@id='introduction']//div//div[@class='introContent']//div[@class='base']//div[@class='content']//ul//li/text()").extract()
        infotransaction = response.xpath(
            "//body//div[@class='m-content']//div[@class='box-l']//div[@id='introduction']//div//div[@class='introContent']//div[@class='transaction']//div[@class='content']//ul//li/text()").extract()
        item['huxing'] = infobase[0]
        item['jianzhumianji'] = infobase[2]
        item['chanquannianxian'] = infobase[12]
        item['fangwuyongtu'] = infotransaction[3]
        item['fangwunianxian'] = infotransaction[4]

    # item['shopname'] = response.xpath(
    #     "//a[@id='supplierName_span']/text()").extract()
    # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
    # item['description'] = response.xpath(
    #     '//td[@id="item_description"]/text()').extract()
        self.log(infobase)
        self.log(infotransaction)
    # yield item
        yield item
# def start_requests(self):

#     urls = [
#         'http://bj.lianjia.com/ershoufang/101101233032.html'
#     ]
#     for url in urls:
#         yield scrapy.Request(url=url, callback=self.parse)

# def parse(self, response):
#     page = response.url.split("/")[-1]
#     filename = 'lianjia-%s' % page
#     # self.log('name %s' % filename)
#     with open(filename, 'wb') as f:
#         f.write(response.body)
#     self.log('Saved file %s' % filename)

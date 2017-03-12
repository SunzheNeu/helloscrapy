#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a spider for lianjia '

__author__ = 'SZ'

import scrapy

class LianjiaSpider(scrapy.Spider):
    name = "lianjiaspider"
    def start_requests(self):
        urls = [
        'http://bj.lianjia.com/ershoufang/101101233032.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'lianjia-%s' % page
        self.log('name %s' % filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

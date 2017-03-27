# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuagualianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    huxing = scrapy.Field()
    jianzhumianji = scrapy.Field()
    chanquannianxian = scrapy.Field()
    fangwuyongtu = scrapy.Field()
    fangwunianxian = scrapy.Field()

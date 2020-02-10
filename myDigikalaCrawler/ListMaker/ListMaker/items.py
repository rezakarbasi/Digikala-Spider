# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ListmakerItem(scrapy.Item):
    name = scrapy.Field()
    cost = scrapy.Field()
    

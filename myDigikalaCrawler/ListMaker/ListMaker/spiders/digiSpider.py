# -*- coding: utf-8 -*-
import scrapy


class DigispiderSpider(scrapy.Spider):
    name = 'digiSpider'
    allowed_domains = ['https://www.digikala.com/search/category-mobile-phone/']
    start_urls = ['http://https://www.digikala.com/search/category-mobile-phone//']

    def parse(self, response):
        pass

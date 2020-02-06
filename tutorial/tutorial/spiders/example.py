# -*- coding: utf-8 -*-
import scrapy
from ..items import TutorialItem
from selenium import webdriver


class ExampleSpider(scrapy.Spider):
    name = 'example'

    start_urls = [
        'https://www.digikala.com/search/category-mobile-phone/?sortby=22']

    def __init__(self):
        self.driver = webdriver.Firefox('/usr/bin/')
        
    def parse(self, response):
        prods = response.css(".is-plp")

        for prod in prods[:2]:
            link = prod.css(".c-product-box__title a::attr(href)").get()
            print('wowww')
            print(link)
            yield response.follow(link, callback=self.parsePage)

    def parsePage(self, response):
        self.driver.get('https://www.example.org/abc')
        
        panel = response.css(".js-c-box-tabs .c-box-tabs__tab")
        link = panel[2].css("a::attr(href)").get()
        
        print('\n\n\n\n\n')
        print('-------------------------page------------------------------------')
        print(panel.css("a::text").extract())
        print(link)
        print('\n\n\n\n\n')
        
        self.driver.close()
        
        yield response.follow(link, callback=self.parseComments)

    def parseComments(self, response):
        print('\n\n\n\n\n\n\n')
        print('##########################commments####################################')
        pass
        # items=TutorialItem()

        # items['cost']=response.css(".js-price-value::text").extract()[0]
        # items['name']=response.css(".c-product__title::text").extract()[0]

        # yield items

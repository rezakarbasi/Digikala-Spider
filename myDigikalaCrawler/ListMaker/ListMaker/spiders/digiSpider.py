import scrapy
from ..items import ListmakerItem

Max_List = 2

# the first url is https://www.digikala.com/search/category-mobile-phone/?pageno=1&sortby=4
firstUrl = 'https://www.digikala.com/search/category-mobile-phone/?pageno='
secondUrl = '&sortby=4'


class DigispiderSpider(scrapy.Spider):
    name = 'digiSpider'
    start_urls = [firstUrl+str(1)+secondUrl]

    def __init__(self):
        self.pageNum = 1
        self.inPage=1

    def parse(self, response):

        print('################################new-page################################')
        prods = response.css(".is-plp")

        i = 0
        for prod in prods:
            print()
            i += 1
            print(i)
            link = prod.css(".c-product-box__title a::attr(href)").get()
            yield response.follow(link, callback=self.parsePage)

        if self.pageNum < Max_List:
            self.pageNum += 1
            newUrl = firstUrl+str(self.pageNum)+secondUrl
            yield response.follow(newUrl, callback=self.parse)

    def parsePage(self, response):
        items=ListmakerItem()
        items['name'] = response.css('.c-product__title::text').extract()[0]
        items['cost'] = response.css('.js-price-value::text').extract()[0]

        items['name'] = response.css('.c-product__title::text').extract()[0]
        items['cost'] = response.css('.js-price-value::text').extract()[0]

        print()
        print('-----------------------new-page-----------------------')
        print(self.inPage)
        self.inPage+=1
        # print(name)
        pass

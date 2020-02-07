import scrapy
from ..items import TutorialItem


Max_List=5

## the first url is https://www.digikala.com/search/category-mobile-phone/?pageno=1&sortby=4
firstUrl='https://www.digikala.com/search/category-mobile-phone/?pageno='
secondUrl='&sortby=4'

class ExampleSpider(scrapy.Spider):
    name = 'example'

    pageNum = 1
    start_urls = [firstUrl+str(1)+secondUrl]

    def parse(self, response):
        print('#####################new list#####################')
        
        prods = response.css(".is-plp")

        for prod in prods:
            link = prod.css(".c-product-box__title a::attr(href)").get()
            yield response.follow(link, callback=self.parsePage)

        if self.pageNum < Max_List:
            self.pageNum += 1
            newUrl = 'https://www.digikala.com/search/category-mobile-phone/?pageno=' + \
                str(self.pageNum)+'&sortby=4'
            yield response.follow(newUrl, callback=self.parse)

    def parsePage(self, response):

        print()
        print('-------------------------page------------------------------------')
        print()

        items = TutorialItem()
        items['name'] = response.css('.c-product__title::text').extract()[0]
        items['cost'] = response.css('.js-price-value::text').extract()[0]

        yield items
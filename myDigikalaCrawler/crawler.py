import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


def crawl_a_page(browser, url, endPage=0):
    maxTry = 30
    tries = 0

    browser.get(url)
    # sleep(2)
    # browser.find_element_by_css_selector('.c-product__engagement-link').click()
    while True:
        try:
            if tries > maxTry:
                return

            browser.find_elements_by_css_selector(
                '.c-box-tabs__tab')[2].click()
            break
        except:
            tries += 1
            pass

    page = 1

    sleep(3)

    if len(browser.find_elements_by_css_selector('.c-pager ul.c-pager__items > li')) == 0:
        return
    maxCommentPage = int(browser.find_element_by_css_selector(
        '.c-pager ul.c-pager__items > li:last-child a').get_attribute('data-page'))

    if endPage == 0:
        endPage = maxCommentPage
    endPage = min(endPage, maxCommentPage)

    n = 0
    tries = 0

    name = browser.find_element_by_css_selector('.c-product__title').text
    
    try:
        price = browser.find_element_by_css_selector('.js-price-value').text
    except:
        price=0

    while page <= endPage:
        tries = 0
        sleep(2)
        try:
            if tries > maxTry:
                return

            for comment_bar in browser.find_elements_by_css_selector('#product-comment-list ul.c-comments__list > li'):
                n += 1

                comment = comment_bar.find_element_by_css_selector(
                    '.article p').text
                data_person = comment_bar.find_element_by_css_selector(
                    '.aside .c-comments__user-shopping').text
                likes = comment_bar.find_element_by_css_selector(
                    '.article .js-comment-like').get_attribute('data-counter')
                dislikes = comment_bar.find_element_by_css_selector(
                    '.article .js-comment-dislike').get_attribute('data-counter')

                yield name, price, comment, data_person, likes, dislikes

        except:
            tries += 1
            pass

        page += 1
        if page > endPage:
            break
        
        pages = browser.find_elements_by_css_selector('.c-pager__items li')
        j = 1

        temp = 0
        while True:
            nexPage = pages[j].find_element_by_css_selector('a')
            if page == int(nexPage.get_attribute('data-page')):
                while True:
                    try:
                        if tries > maxTry:
                            return

                        nexPage.click()
                        temp = 1
                        break
                    except:
                        tries += 1

                        sleep(3)
                        pass
                break
            j += 1
            if temp > 0:
                break


numPagesList = 3

browser = webdriver.Chrome('/usr/bin/chromedriver')

# for a in crawl_a_page(browser, 'https://www.digikala.com/product/dkp-2117141/'):
#     print(a)

firstUrl = 'https://www.digikala.com/search/category-mobile-phone/?pageno='
secondUrl = '&sortby=4'

prodUrls = []

for i in range(numPagesList):
    url = firstUrl+str(i+1)+secondUrl
    browser.get(url)

    for element in browser.find_elements_by_css_selector('.c-product-box__content--row .c-product-box__title'):
        prodUrls += [element.find_element_by_css_selector(
            'a').get_attribute('href')]

saveData = {'name': [], 'price': [], 'comment': [],
            'data_person': [], 'likes': [], 'dislikes': []}
pd.DataFrame(saveData).to_csv('crawled2.csv', header=True)

for url in prodUrls:
    saveData = {'name': [], 'price': [], 'comment': [],
                'data_person': [], 'likes': [], 'dislikes': []}
    for name, price, comment, data_person, likes, dislikes in crawl_a_page(browser, url, 10):
        saveData['name'] += [name]
        saveData['price'] += [price]
        saveData['comment'] += [comment]
        saveData['data_person'] += [data_person]
        saveData['likes'] += [likes]
        saveData['dislikes'] += [dislikes]
    pd.DataFrame(saveData).to_csv('crawled2.csv', header=False, mode='a')

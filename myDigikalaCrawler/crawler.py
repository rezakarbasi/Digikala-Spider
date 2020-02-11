import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

def crawl_a_page(browser, url):
    maxTry = 30

    browser.get(url)
    sleep(1)
    browser.find_element_by_css_selector('.c-product__engagement-link').click()

    page = 1

    sleep(3)

    endPage = int(browser.find_element_by_css_selector(
        '.c-pager ul.c-pager__items > li:last-child a').get_attribute('data-page'))
    n = 0
    tries = 0

    while page <= endPage:
        tries = 0
        sleep(2)
        try:
            if tries > maxTry:
                break

            for i in range(1, 16):
                n += 1
                st = '#product-comment-list ul.c-comments__list > li:nth-child('+str(
                    i)+')'
                comment = browser.find_element_by_css_selector(
                    st+' .article p').text
                data_person = browser.find_element_by_css_selector(
                    st+' .aside .c-comments__user-shopping').text
                likes = browser.find_element_by_css_selector(
                    st+' .article .js-comment-like').get_attribute('data-counter')
                dislikes = browser.find_element_by_css_selector(
                    st+' .article .js-comment-dislike').get_attribute('data-counter')

                yield comment, data_person, likes, dislikes

        except:
            tries += 1
            pass

        page += 1
        pages = browser.find_elements_by_css_selector('.c-pager__items li')
        j = 1
        
        temp=0
        while True:
            nexPage = pages[j].find_element_by_css_selector('a')
            if page == int(nexPage.get_attribute('data-page')):
                while True:
                    try:
                        if tries > maxTry:
                            break

                        nexPage.click()
                        temp=1
                        break
                    except:
                        tries += 1

                        sleep(1)
                        pass
                break
            j += 1
            if temp>0:
                break


# if __name__ == "__main__":
browser = webdriver.Chrome('/usr/bin/chromedriver')
url = 'https://www.digikala.com/product/dkp-2117141/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-note-8-m1908c3jg-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
    
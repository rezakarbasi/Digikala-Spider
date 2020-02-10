import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep


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
        pages = browser.find_element_by_css_selector('.c-pager__items')
        j = 2

        while True:
            nexPage = pages.find_element_by_css_selector(
                'ul > li:nth-child('+str(j) + ') a')
            if page == int(nexPage.get_attribute('data-page')):
                while True:
                    try:
                        if tries > maxTry:
                            break

                        nexPage.click()
                        break
                    except:
                        tries += 1

                        sleep(2)
                        pass
                break
            j += 1

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

while 1:
    browser = webdriver.Chrome()

    browser.get('https://ece391test.web.illinois.edu/queue/demo')
    browser.implicitly_wait(0.5)

    login = browser.find_elements_by_class_name("nav-link")[3]
    ActionChains(browser).click(login).perform()
    browser.find_element_by_id("j_username").send_keys('shiqiyu2')
    browser.find_element_by_id("j_password").send_keys('Yusq1998!!!!')

    login_illinois = browser.find_element_by_xpath('//*[@id="submit_button"]/input').click()

    en_q = browser.find_elements_by_class_name("nav-link")[1]
    ActionChains(browser).click(en_q).perform()

    browser.find_element_by_css_selector('#newq_h').click()

    try:
        browser.find_element_by_css_selector('#new_question > button').click()
    except selenium.common.exceptions.NoSuchElementException:
        browser.close()
        continue





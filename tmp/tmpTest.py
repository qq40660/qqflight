#-*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from common import *

driver = webdriver.Firefox()

url = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate=20131107'

driver.get(url)
destination = driver.find_element_by_xpath("//*[@id='tripWayGo']/h3/a").text[-6:-1]
print destination
dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[2]/a/strong"
driver.find_element_by_xpath(dateElemnet).click()
time.sleep(3)
print u"日期选择完毕"
startTime = driver.find_element_by_xpath("\
        //*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')
print "start time is: %s" % startTime[-8:]

driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()
        #得到下拉报价区的ota数量
x = len(driver.find_elements(By.XPATH, "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr"))
print x
for i in range(1, x):
    flightListTable = "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr[%s]/td[2]" % i
    keyWords = driver.find_element_by_xpath(flightListTable).text[:4]
    print keyWords


"""
def getKeyWordsPresent():
    try:
        driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()
        #得到下拉报价区的ota数量
        x = len(driver.find_elements(By.XPATH, "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr"))
        for i in range(1, x):
            flightListTable = "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr[%s]/td[2]"
            keyWords = driver.find_element_by_xpath(flightListTable).text[:4]
            return keyWords
    except:
        print 1111111111111111

for url in urlList:
    driver.get(url)
    destination = driver.find_element_by_xpath("//*[@id='tripWayGo']/h3/a").text[-6:-1]
    print destination
    for i in range(1, 8):
        dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        time.sleep(3)
        print u"日期选择完毕"
        getKeyWordsPresent()
        if i == 7:
            startTime = driver.find_element_by_xpath("\
                    //*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]

        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]

    for i in range(5, 8):
        dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        getKeyWordsPresent()
        time.sleep(3)
        print 1
        if i == 7:
            startTime = driver.find_element_by_xpath("\
                    //*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]
        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]

"""



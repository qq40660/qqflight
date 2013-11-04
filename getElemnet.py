#-*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


def getdateElement():
    driver = webdriver.Firefox()
    driver.get('http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate=20131104')
    for i in range(1, 8):
        dateElemnet = "//*[@id='daysLowest']/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()
        print 1
        if i == 7:
            startTime = driver.find_element_by_xpath("//*[@id='daysLowest']/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]
        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]
    for i in range(5, 8):
        dateElemnet = "//*[@id='daysLowest']/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        time.sleep(3)
        print 1
        if i == 7:
            startTime = driver.find_element_by_xpath("//*[@id='daysLowest']/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]
        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]
getdateElement()

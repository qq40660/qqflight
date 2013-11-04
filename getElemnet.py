#-*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Firefox()


def getdateElement():

    driver.get('http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate=20131104')
    for i in range(1, 8):
        dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        print 1
        if i == 7:
            startTime = driver.find_element_by_xpath("//*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]
        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]
    for i in range(5, 8):
        dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElemnet).click()
        time.sleep(3)
        print 1
        if i == 7:
            startTime = driver.find_element_by_xpath("//*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')
            print startTime[-8:]
        else:
            startTime = driver.find_element_by_xpath(dateElemnet).get_attribute('id')
            print startTime[-8:]
getdateElement()


def getKeyWordsPresent():
    driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()

    #得到下拉报价区的ota数量
    x = len(driver.find_elements(By.XPATH, "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr"))
    for i in range(1, x):
        flightListTable = "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr[%s]/td[2]"
        keyWords = driver.find_element_by_xpath(flightListTable).text[:4]
        print keyWords

    pass
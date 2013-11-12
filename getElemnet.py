#-*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sendMail import *

from common import *

start = time.time()
driver = webdriver.Firefox()

#url = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate=20131104'

urlList = get_url()


def getKeyWordsPresent():
    try:
        driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()
        global flightNo
        flightNo = driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[1]").text
        print flightNo
        global airlineFlightNo
        airlineFlightNo = flightNo[:4] + flightNo[5:]
        print 'Fli'
        print airlineFlightNo
        #得到下拉报价区的ota数量
        global otaCount
        otaCount = len(driver.find_elements(By.XPATH, "\
            //*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr"))
        global keyWordsCount
        keyWordsCount = 0
        for i in range(1, (otaCount + 1)):
            flightListTable = "//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr[%s]/td[2]" % i
            keyWords = driver.find_element_by_xpath(flightListTable).text[:4]
            if keyWords == u'酷讯担保':
                keyWordsCount += 1
            print keyWords, keyWordsCount
        if keyWordsCount < 2 and otaCount == 3:
            print "Error"
            send_error_mail(MAIL_TO, destination, startTime, flightNo)
        #return airlineFlightNo, otaCount, keyWordsCount
    except:
        print u"无法找到"


for url in urlList:
    driver.get(url)
    destination = driver.find_element_by_xpath("//*[@id='tripWayGo']/h3/a").text[-6:-1]
    print destination

    for i in range(1, 8):
        dateElement = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElement).click()
        time.sleep(3)
        print u"日期选择完毕"
        getKeyWordsPresent()
        if i == 7:
            try:
                startTime = driver.find_element_by_xpath("\
                        //*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')[-8:]
                write_to_log(destination, airlineFlightNo, startTime, otaCount, keyWordsCount)
                print startTime
            except:
                no_flight(destination)
        else:
            try:
                startTime = driver.find_element_by_xpath(dateElement).get_attribute('id')[-8:]
                write_to_log(destination, airlineFlightNo, startTime, otaCount, keyWordsCount)
                print startTime
            except:
                no_flight(destination)

    for i in range(5, 8):

        dateElement = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[%s]/a/strong" % i
        driver.find_element_by_xpath(dateElement).click()
        time.sleep(3)
        print u"日期选择完毕"
        getKeyWordsPresent()
        time.sleep(3)
        print 1
        if i == 7:
            try:
                startTime = driver.find_element_by_xpath("\
                        //*[@class='ticket_main_select']/div[1]/ul[1]/li[4]/a/strong").get_attribute('id')[-8:]
                write_to_log(destination, airlineFlightNo, startTime, otaCount, keyWordsCount)
                print startTime
            except:
                no_flight(destination)
        else:
            try:
                startTime = driver.find_element_by_xpath(dateElement).get_attribute('id')[-8:]
                write_to_log(destination, airlineFlightNo, startTime, otaCount, keyWordsCount)
                print startTime
            except:
                no_flight(destination)
end = time.time()
elapsed = end - start
print "Time taken: ", elapsed, "seconds."



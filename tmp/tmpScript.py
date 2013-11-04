#-*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=XMN&depDate=20131105&qf=go.qq.com%2Fflight%2Fl'

driver = webdriver.Firefox()
driver.get(url)

dateElemnet = "//*[@class='ticket_main_select']/div[1]/ul[1]/li[1]/a/strong"
driver.find_element_by_xpath(dateElemnet).click()

driver.find_element_by_xpath("//*[@id='flightListTable']/tbody/tr[1]/td[6]/a/span").click()

try:
    webdriver.assertEqual(u"很抱歉，没有找到符合您查询条件的航班", driver.find_element_by_css_selector("p.single_row").text)
except AssertionError as e:
    webdriver.verificationErrors.append(str(e))

#driver.find_element_by_xpath(".//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody")
#得到下拉报价区的ota数量
"""
x = driver.find_element_by_xpath(".//*[@id='flightListTable']/tbody/tr[2]/td/div[1]/div[2]/table/tbody/tr[1]/td[2]").text[:4]
print x

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://go.qq.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):

        driver = self.driver
        driver.get(self.base_url + "/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=XMN&depDate=20131105&qf=go.qq.com%2Fflight%2F")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.single_row"))
        except AssertionError as e: self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

"""
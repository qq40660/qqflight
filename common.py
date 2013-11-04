#-*- coding:utf8 -*-

from dataCalculate import *
"""
访问的url为head + 日期到计算函数。
"""



bhHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=SHA&depDate='
bgHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=PEK&toCity=CAN&depDate='
hgHead = 'http://go.qq.com/v2/flight/list.html?tripType=0&fromCity=SHA&toCity=CAN&depDate='

urlHeadList = [bhHead, bgHead, hgHead]
urlList = []

for i in urlHeadList:
    for x in getDataList():
        urlList.append(i+x)








#-*- coding:utf8 -*-

import time

"""
1. 先计算当前月份的日期
2. 根据日期计算10天内到日期
"""

today = time.strftime('%Y-%m-%d', time.gmtime())
year = int(today[:4])
month = int(today[5:7])
day = int(today[-2:])


def __getDays():
    #定义每月最多的天数
    dayAmount = 31
    while day:
        try:
            #尝试将这个月最大的天数的字符串进行转化
            time.strptime('%s-%s-%d' % (year, month, dayAmount), '%Y-%m-%d')
            #成功时返回得就是这个月的天数
            return dayAmount
        except:
            #否则将天数减1继续尝试转化, 直到成功为止
            dayAmount -= 1


def getDataList():
    thisMonthDays = __getDays()
    dateList = []
    if day + 10 > thisMonthDays:
        enddays = (day + 10 - thisMonthDays)
        monthNext = month + 1
        if monthNext > 12:
            yearNext = year + 1
            monthNext -= 12
            if monthNext < 10:
                monthNext = str(0) + str(monthNext)
        for i in xrange(day, thisMonthDays + 1):
            dateListStr = str(year) + str(month) + str(i)
            dateList.append(dateListStr)
        if enddays == 1:
            tmpdate = str(0) + str(enddays)
            dateListStr = str(yearNext) + str(monthNext) + str(tmpdate)
            dateList.append(dateListStr)
        else:
            for i in xrange(1, enddays):
                if i < 10:
                    i = str(0) + str(i)
                dateListStr = str(yearNext) + str(monthNext) + str(i)
                dateList.append(dateListStr)
        return dateList
    else:
        for i in xrange(day, (day+10)):
            if i < 10:
                i = str(0) + str(i)
            dateListStr = str(year) + str(month) + str(i)
            dateList.append(dateListStr)

    return dateList

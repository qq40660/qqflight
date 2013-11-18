#-*- coding:utf8 -*-

from config import *
from sendMail import *
import time


urlHeadList = [bhHead, bgHead, hgHead]
urlTmpList = []
urlDate = time.strftime('%Y%m%d')


def get_url():

    for i in urlHeadList:
        urlTmpList.append(i+urlDate)
    return urlTmpList


def write_to_log(destination='Null', flightNo='Null', startTime='Null', otaCount='Null', keyWordsPresent='Null'):

    #fileHandle = open('/root/PycharmProjects/qqflight/log/log', 'a')
    fileHandle = open('E:\Workspaces\qqflight\log\log', 'a')
    scriptRunTime = time.strftime('%Y-%m-%d %H-%M')
    stringInput = 'RunTime: %s, Destination: %s, FlightNo: %s, startTime: %s, OTAAmount: %s, keyWords: %s' \
                  % (scriptRunTime, destination, flightNo, startTime, otaCount, keyWordsPresent)
    fileHandle.write(stringInput.encode('utf-8'))
    fileHandle.write('\n')
    fileHandle.close()


def no_flight(destination='Null'):

    #fileHandle = open('/root/PycharmProjects/qqflight/log/log', 'a')
    fileHandle = open('E:\Workspaces\qqflight\log\log', 'a')
    scriptRunTime = time.strftime('%Y-%m-%d %H-%M')
    stringInput = 'RunTime: %s, Destination: %s. No flight in this time' % (scriptRunTime, destination)
    fileHandle.write(stringInput.encode('utf-8'))
    fileHandle.write('\n')
    fileHandle.close()


"""
#脚本运行时间计算
start = time.time()
end = time.time()
elapsed = end - start
print "Time taken: ", elapsed, "seconds."
"""


#-*- coding:utf8 -*-

from config import *
import time


urlHeadList = [bhHead, bgHead, hgHead]
urlTmpList = []
urlDate = time.strftime('%Y%m%d', time.gmtime())


def get_url():

    for i in urlHeadList:
        urlTmpList.append(i+urlDate)
    return urlTmpList


def write_to_log(destination, flightNo, otaCount):
    fileHandle = open('/root/PycharmProjects/qqflight/log', 'a')
    scriptRunTime = time.strftime('%Y-%m-%d %H-%M')
    stringInput = 'RunTime: %s, Destination: %s, FlightNo: %s, OTAAmount: %s, keyWords:' \
                  % (scriptRunTime, destination, flightNo, otaCount)
    file.write(stringInput)
    fileHandle.close()

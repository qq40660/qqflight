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






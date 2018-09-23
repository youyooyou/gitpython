#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 21:06
# @Author   : youyooyou@126.com
# @File     : strDefined.py
# @Software : PyCharm
# @ModifyLog:


def awHassamechar(str):
    '''
    :param str:输入一个字符串
    :return:str中有重复的字符返回True，否则返回False
    '''
    result = True
    strList = list(str)
    strLen = len(strList)
    for i in range(0, strLen):
        if str.count(strList[i]) != 1:
            result = True
            break
        else:
            result = False
    return result
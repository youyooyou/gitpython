#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 20:50
# @Author   : youyooyou@126.com
# @File     : mathDefined.py
# @Software : PyCharm
# @ModifyLog:

def awIsAlpha(str):
    '''
    :param str:
    :return:全是字母（不区分大小写）则返回True，否则返回False
    '''
    return str.isalpha()

def awIsDigit(str):
    '''
    :param str:
    :return: 是数字则返回True，否则返回False
    '''
    return str.isdigit()

def awIsInt(num):
    '''
    :param num:
    :return: 是整数则返回True，否则返回False
    '''
    if isinstance(num, int):
        return True
    return False

def awSort(digitList):
    if not isinstance(digitList, list):
        raise "输入参数为list，请以list作为入参输入。"
    return digitList.sort()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 22:16
# @Author   : youyooyou@126.com
# @File     : timeDefined.py
# @Software : PyCharm
# @ModifyLog:

from commonFunc.mathDefined import *

monthDay = {1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}

leapYear = 1

def awIsLeapyear(year):
    '''
    :param year: 正整数
    :return: 是闰年则返回True，否则返回False
    '''
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

def awIsLigal(year, month, day):
    '''
    :param year:
    :param month:
    :param day:
    :return:
    '''
    result = True
    # 判断year
    if not awIsInt(year) or year <= 0:
        print("输入参数不合法！\r\n请输入有效的年份。")
        result = False
    # 判断month
    if month not in monthDay.keys():
        print("输入参数不合法！\r\n请输入有效的月份。")
        result = False
    # 判断day
    if awIsLeapyear(year) and month == 2:
        if day not in range(1, monthDay[2] + 2):
            print("输入参数不合法！\r\n请输入有效的日期。")
            result = False
    else:
        if day not in range(1, monthDay[month] + 1):
            print("输入参数不合法！\r\n请输入有效的日期。")
            result = False
    return result

def awCalcDay(year, month, day):
    '''
    :param year:
    :param month:
    :param day:
    :return: 返回该年的第几天
    '''
    if not awIsLigal(year, month, day):
        raise "输入参数不合法。"
    result = day
    for i in range(1, month):
        result += monthDay[i]
    if awIsLeapyear(year):
        result += 1
    return result


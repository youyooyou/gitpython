#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 21:39
# @Author   : youyooyou@126.com
# @File     : testCase.py
# @Software : PyCharm
# @ModifyLog:

from commonFunc.mathDefined import *
from commonFunc.strDefined import *


class case():
    def case_001(self, num1, num2, num3, num4):
        '''
        :param num1: 输入的第一个整数
        :param num2: 输入的第二个整数
        :param num3: 输入的第三个整数
        :param num4: 输入的第四个整数
        :return: 无返回值，函数内部打印不同组合
        题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
        '''
        if awIsInt(num1) and awIsInt(num2) and awIsInt(num3) and awIsInt(num4):
            strList = [str(num1), str(num2), str(num3), str(num4)]
            strLen = len(strList)
            for i in range(0, strLen):
                for j in range(0, strLen):
                    for k in range(0, strLen):
                        tmpStr = strList[i] + strList[j] + strList[k]
                        if not awHassamechar(tmpStr):
                            print(tmpStr)
        else:
            print("输入参数有误！\r\n输入参数需要全部是整数，请检查输入参数是否均为整数。")
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 20:36
# @Author   : youyooyou@126.com
# @File     : start.py
# @Software : PyCharm
# @ModifyLog:


def _test():
    from python_100case import testCase

    case = testCase.case()
    case.case_001(num2=9, num1=2, num4=3, num3=4)


if __name__ == '__main__':
    _test()
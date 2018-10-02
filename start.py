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
    #case.case_002("sfd")
    #case.case_004(2018, 9, 24)
    case.case_005(1, 2, 3)


if __name__ == '__main__':
    _test()
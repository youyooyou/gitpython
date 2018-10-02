#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/23 21:39
# @Author   : youyooyou@126.com
# @File     : testCase.py
# @Software : PyCharm
# @ModifyLog:

from commonFunc.mathDefined import *
from commonFunc.strDefined import *
from commonFunc.timeDefined import *


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


    def case_002(self, digitInput):
        '''
        :param digitInput:输入利润
        :return:返回奖金总数
        题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
        程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
        '''
        if not awIsDigit(digitInput):
            raise "输入参数不正确！请输入一个有效的正数。"

    def case_003(self):
        '''
        :return:
        题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

        程序分析：
        假设该数为 x。
        1、则：x + 100 = n2, x + 100 + 168 = m2
        2、计算等式：m2 - n2 = (m + n)(m - n) = 168
        3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
        4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
        5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
        6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
        7、接下来将 i 的所有数字循环计算即可。
        '''
        pass

    def case_004(self, year, month, day):
        '''
        :param year:
        :param month:
        :param day:
        :return:
        题目：输入某年某月某日，判断这一天是这一年的第几天？
        程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
        '''
        print(year.__str__() + "年的第" + awCalcDay(year, month, day).__str__() + "天。")

    def case_005(self, x, y, z):
        '''
        :param x:
        :param y:
        :param z:
        :return:
        题目：输入三个整数x,y,z，请把这三个数由小到大输出。
        程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
        '''
        if not awIsDigit(x) or not awIsDigit(y) or not awIsDigit(z):
            print("输入参数不正确！\r\n请输入有效的数字。")
        print(awIsDigit(x, y, z))

    def case_006(self, n):
        '''
        :param n:
        :return:
        斐波那契数列
        F0 = 0     (n=0)
        F1 = 1    (n=1)
        Fn = F[n-1]+ F[n-2](n=>2)
        '''
        result = 0
        if not isinstance(n, int):
            print("INPUT ERR")
        if n == 0:
            result = 0
            return result
        if n == 1:
            result = 1
            return result
        else:
            self.case_006(n - 1) + self.case_006(n - 2)
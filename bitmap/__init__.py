#!/usr/bin/python
# -*- coding: utf-8 -*-


# @Time    : 2020/5/20 9:33 AM
# @Author  : fanding
# @FileName: demo.py
# @Software: PyCharm
# @微信公众号: 樊樊家园

'''
位图数据结构

布隆过滤器是位图数据结构的一种优化，核心思想是利用多个hash函数对数据进行多次hash，
布隆过滤器适用场景：
    1、具有一定容错的场景
    2、去重的时候涉及到的数据量特别大

怎样降低布隆过滤器去重时候的错误率：
一、已知数据量情况。
    位图大小适当大点。
二、未知数据量情况。
    支持自动扩容，防止数据量逐渐增大而造成很高的错误率。
'''


class Bitmap(object):
    def __init__(self, max):
        '''
        :param max: 要表示的最大整数
        '''
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]
        self.memory = (self.size * 4) / (1024 * 1024 * 1024)

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return num / 31

    def calcBitIndex(self, num):
        return num % 31

    def set(self, num):
        '''
        :param num: 将某个数添加到位图中（将对应的二进制位置为1）
        '''
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        '''
        :param i: 将某个数从位图中移除出去（将对应的二进制位置为0）
        '''
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))

    def test(self, i):
        '''
        :param i: 要检测的数字
        :return: 如果数字存在位图中则返回True，否则返回False
        '''
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False

    def __str__(self):
        data = {
            'G': self.memory,
            'M': self.memory * 1024,
            'KB': self.memory * 1024 * 1024,
            'B': self.memory * 1024 * 1024 * 1024
        }
        infoList = []
        infoList.append('*************************')
        for key, value in data.items():
            infoList.append(str(value) + ' ' + key)
        infoList.append('*************************')
        info = '\n'.join(infoList)
        return info


if __name__ == '__main__':
    bitmap = Bitmap(10000000000)
    print(bitmap.size)
    print(bitmap)

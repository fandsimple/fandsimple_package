#!/usr/bin/python
# -*- coding: utf-8 -*-


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

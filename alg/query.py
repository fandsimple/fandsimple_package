#!/usr/bin/python
# -*- coding: utf-8 -*-


def bserach(dataList, n, value): # 二分查找递归实现
    def bserachTemp(dataList, startIndex, endIndex, value):
        if startIndex > endIndex:
            return -1
        midIndex = (startIndex + endIndex) // 2
        if dataList[midIndex] > value:
            return bserachTemp(dataList, startIndex, midIndex - 1, value)
        elif dataList[midIndex] < value:
            return bserachTemp(dataList, midIndex + 1, endIndex, value)
        elif dataList[midIndex] == value:
            return midIndex

    index = bserachTemp(dataList, 0, n - 1, value)
    return index


if __name__ == '__main__':
    dataList = [1, 4, 6, 7, 34, 45, 56]
    print(bserach(dataList, len(dataList), 56))

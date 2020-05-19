#!/usr/bin/python
# -*- coding: utf-8 -*-


def bserach(dataList, n, value):  # 二分查找递归实现
    '''
    注意：
        1、dataList中不能出现重复元素。
        2、如果只查询dataList中是否出现value值，是可以出现重复值的。
    时间复杂度：
        O(logn)
    空间复杂度：
        O(1)
    '''

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


def bserachFirst(dataList, n, value):  # 在dataList中查找第一个为value的元素
    objIndex = bserach(dataList, n, value)
    if objIndex == -1:
        return -1
    i = objIndex - 1
    while i >= 0:
        if dataList[i] != value:
            break
        i -= 1
    return i + 1

def bserachLast(dataList, n, value):  # 在dataList中查找最后一个为value的元素
    objIndex = bserach(dataList, n, value)
    if objIndex == -1:
        return -1
    i = objIndex + 1
    while i < n:
        if dataList[i] != value:
            break
        i += 1
    return i - 1


if __name__ == '__main__':
    dataList = [4, 5, 5, 6, 6, 34, 56, 56]

    # print(bserach(dataList, len(dataList), 56))

    # print(bserachFirst(dataList, len(dataList), 56))

    print(bserachLast(dataList, len(dataList), 4))

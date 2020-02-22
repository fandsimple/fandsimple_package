#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
冒泡排序：
插入排序：
选择排序：


'''


def bubbleSort(dataList, n):  # 冒泡排序
    '''
    最短时间复杂度：O(n)
    最长时间复杂度：O(n*n)
    平均时间复杂度：O(n*n)
    空间复杂度：O(1)-->原地排序
    稳定排序：是
    '''
    for i in range(n):
        isSwap = False
        for j in range(n - i - 1):
            if dataList[j] > dataList[j + 1]:
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
                isSwap = True
        if not isSwap:
            break


def insertSort(dataList, n):  # 插入排序
    '''
    最短时间复杂度：O(n)
    最长时间复杂度：O(n*n)
    平均时间复杂度：O(n*n)
    空间复杂度：O(1)-->原地排序
    稳定排序：是
    '''
    if n <= 1:
        return
    for i in range(1, n):
        temp = dataList[i]
        for j in range(i - 1, -1, -1):  #
            if temp < dataList[j]:
                dataList[j + 1] = dataList[j]
            else:
                break
        dataList[j + 1] = temp


def selectSort(dataList, n): # 选择排序
    '''
    最短时间复杂度：O(n*n)
    最长时间复杂度：O(n*n)
    平均时间复杂度：O(n*n)
    空间复杂度：O(1)-->原地排序
    稳定排序：不稳定
    总结：这孙子是最'稳定'的一个排序算法
    '''
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if dataList[i] > dataList[j]:
                minIndex = j
        dataList[i], dataList[minIndex] = dataList[minIndex], dataList[i]




if __name__ == '__main__':
    dataList = [1, 2, 5, 3, 6, 2]

    # bubbleSort(dataList, len(dataList))
    # print(dataList)

    # insertSort(dataList, len(dataList))
    # print(dataList)

    selectSort(dataList, len(dataList))
    print(dataList)

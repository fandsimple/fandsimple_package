#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
冒泡排序：略
插入排序：略
选择排序：略
归并排序：
    时间复杂度分析：
        参考代码逻辑，利用递归思想解决时间复杂度。
    空间复杂度分析：
        cpu同一时刻只能执行一个递归函数，每个递归函数中需要最大大小为dataList长度的空间，
        但是当调出函数时就被释放掉了，所以整体来说空间复杂度为O(n)
快速排序：
    时间复杂度分析：
        最好O(nlogn)、 平均O(nlogn)、 最差O(n*n)
    空间复杂度分析：
        原地排序
桶排序：
    时间复杂度：
        O(n)
    空间复杂度：
        O(n)
    稳定性：
        稳定
    应用场景：
        解决排序时无法一次性将数据读入内存中，在磁盘上分成不同的有序桶，然后将每个桶内数据
        进行排序即可。（可能桶中的数据分布不均匀）
计数排序：
    时间复杂度：
        O(n)
    空间复杂度：
        O(n + k)
        k: 要排序的数据范围
    稳定性：
        稳定
    使用场景：
        非负整数、数据规模远远大于所要处理的数据范围，（年龄、成绩等等）

基数排序：
    时间复杂度：
        d：数据位数，如手机号d=11
        O(dn)
    空间复杂度：
        非原地排序
    稳定性：
        稳定
    使用场景：
        基数排序要求数据可以划分成高低位，位之间有递进关系。比较两个数，我
        们只需要比较高位，高位相同的再比较低位。而且每一位的数据范围不能太
        大，因为基数排序算法需要借助桶排序或者计数排序来完成每一个位的排序工作。
        例子：大量手机号排序，大规模日志按时间排序。
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


def selectSort(dataList, n):  # 选择排序
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


def mergeSort(dataList, n):
    '''
    最短时间复杂度：O(nlogn)
    最长时间复杂度：O(nlogn)
    平均时间复杂度：O(nlogn)
    空间复杂度：O(n)
    稳定排序：是
    '''

    def merge(a, low, mid, high):
        i, j = low, mid + 1
        tmp = []
        while i <= mid and j <= high:
            if a[i] <= a[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(a[j])
                j += 1
        start = i if i <= mid else j
        end = mid if i <= mid else high
        tmp.extend(a[start:end + 1])
        a[low:high + 1] = tmp

    def merge_sort_between(dataList, low, high):
        if low < high:
            mid = low + (high - low) // 2
            merge_sort_between(dataList, low, mid)
            merge_sort_between(dataList, mid + 1, high)
            merge(dataList, low, mid, high)

    return merge_sort_between(dataList, 0, n - 1)


def quickSort(dataList, n):  # 快速排序
    '''
    最短时间复杂度：O(nlogn)
    最长时间复杂度：O(nlogn)
    平均时间复杂度：O(n*n)
    空间复杂度：原地排序
    稳定排序：不稳定
    '''

    def partition(dataList, startIndex, endIndex):  # 将一个元素寻找到排序后的位置
        last = dataList[endIndex]
        j = startIndex  # j索引前方的值都比last小
        i = startIndex
        while i < endIndex:
            if dataList[i] < last:
                dataList[i], dataList[j] = dataList[j], dataList[i]
                j += 1
            i += 1
        dataList[i], dataList[j] = dataList[j], dataList[i]
        return j

    def quickSortTemp(dataList, startIndex, endIndex):
        if startIndex >= endIndex:
            return
        postion = partition(dataList, startIndex, endIndex)
        quickSortTemp(dataList, startIndex, postion - 1)
        quickSortTemp(dataList, postion + 1, endIndex)

    quickSortTemp(dataList, 0, n - 1)


# 堆排序
def heapSort(dataList, n):
    '''
    时间复杂度：O(nlogn)
    空间复杂度：O(1)
    稳定性：不稳定
    '''
    def heapify(dataList, n, i):  # 堆化函数
        if len(dataList) == 0:
            return
        max = i
        while True:
            if i * 2 <= n and dataList[i] < dataList[i * 2]:
                max = i * 2
            if (i * 2 + 1) <= n and dataList[max] < dataList[i * 2 + 1]:
                max = i * 2 + 1
            if max == i:
                break
            dataList[i], dataList[max] = dataList[max], dataList[i]
            i = max

    def createHeap(dataList, n): # 建堆
        for i in range((n // 2), 0, -1):
            heapify(dataList, n, i)

    createHeap(dataList, n)
    for i in range(n, 0, -1): # 调用以上函数进行排序
        dataList[1], dataList[i] = dataList[i], dataList[1]
        heapify(dataList, i-1, 1)





def bucketSort(dataList, n):  # 桶排序
    '''
    时间复杂度：O(n)
    空间复杂度：O(n)
    稳定排序：稳定的
    '''
    pass


def countSort(dataList, n):  # 计数排序
    '''
    k: 要排序数据范围
    最短时间复杂度：O(n+k)
    空间复杂度：O(n+k)
    稳定排序：稳定
    '''

    def getRange(dataList):  # 获取要排序数据范围minIndex、maxIndex
        minIndex = min(dataList)
        maxIndex = max(dataList)
        return maxIndex - minIndex + 1

    def countData(dataList):  # 统计 + 处理成对照表
        num = getRange(dataList)
        countList = [0] * num
        for i in dataList:
            countList[i - 1] += 1
        for j in range(num):
            if j == 0:
                continue
            countList[j] = countList[j] + countList[j - 1]
        return countList

    countList = countData(dataList)
    tempList = [None] * n
    for i in range(n - 1, -1, -1):
        countList[dataList[i] - 1] -= 1
        tempList[countList[dataList[i] - 1]] = dataList[i]
    dataList[:] = tempList


def radixSort(dataList, n):
    '''
    间复杂度：O(dn)
    空间复杂度：非原地排序
    稳定排序：稳定
    '''
    pass


if __name__ == '__main__':
    dataList = [10, 2, 4, 3, 8, 6, 5, 3]

    # bubbleSort(dataList, len(dataList))
    # print(dataList)

    # insertSort(dataList, len(dataList))
    # print(dataList)

    # selectSort(dataList, len(dataList))
    # print(dataList)

    # mergeSort(dataList, len(dataList))
    # print(dataList)

    # quickSort(dataList, len(dataList))
    # print(dataList)

    # countSort(dataList, len(dataList))
    # print(dataList)

    # 堆排序测试
    # dataList = [None, 2, 4, 3, 8, 6, 5, 3] # 注意第一个不存储元素
    # heapSort(dataList, len(dataList)-1)
    # print(dataList)

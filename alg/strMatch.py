#!/usr/bin/python
# -*- coding: utf-8 -*-


# BF字符窜匹配算法
def strMatchBF(str, patternStr):  # 暴力查找
    '''
    时间复杂度：O(n*m)
    :param str: 主串
    :param patternStr: 模式串
    :return: 如果匹配成功返回模式串在主串中第一次出现的位置，如果查找不到返回-1.
    '''
    for i in range(len(str) - len(patternStr) + 1):
        for j in range(len(patternStr)):
            if str[i + j] != patternStr[j]:
                break
        else:
            return i
    return -1


# RK字符串匹配算法
def strMatchRK(str, patternStr):
    pass


# BM算法
def strMatchBM(str, patternStr):
    n = len(str)
    m = len(patternStr)

    # 为patternStr构建散列表
    charToIndexMap = {}
    for index, s in enumerate(patternStr):
        charToIndexMap[s] = index  # 如果有相同字符的会覆盖，这于坏字符匹配思想一直（如果字符相同，最终取索引靠后的那一个）

    i = 0

    while i < (n - m):  # 最多移到n-m-1索引的位置
        j = m - 1  # 按照patternStr串倒着来匹配
        while j >= 0:
            if str[i + j] != patternStr[j]:  # 如果是不相等的情况下坏字符的位置就找到了，记录坏字符在patternStr中的位置
                si = j  # 讲义中的si变量
                xi = charToIndexMap[str[i + j]]  # 寻找xi的值
                break
            j -= 1
        if j == -1:  # 如果一直str[i + j] 和 patternStr[j]相等下去，j最终会变为-1故找到匹配的子串了， 直接返回
            return i
        # 通过坏字符串规则重新定义i的值
        i += (si - xi)
    return -1


# 构建两个数组
def createTem(patternStr, m, suffixList, prefixList):
    for i in range(m):
        suffixList[i] = -1
        prefixList[i] = False

    for i in range(m):
        j = i
        k = 0
        while j >= 0 and patternStr[j] == patternStr[m - 1 - k]:
            j -= 1
            k += 1
            suffixList[k] = j + 1


if __name__ == '__main__':
    # str1 = '123456789'
    # str2 = '890'
    # print(strMatchBF(str1, str2))

    patternStr = 'abcdfab'
    suffixList = [None] * len(patternStr)
    prefixList = [None] * len(patternStr)

    createTem(patternStr, len(patternStr), suffixList, prefixList)
    print(suffixList)
    print(prefixList)

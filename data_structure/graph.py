#!/usr/bin/python
# -*- coding: utf-8 -*-
from data_structure import SingleLinkList


class UndiGraph(): # 无向图
    def __init__(self, size=100):
        self.size = size
        self.dataList = []
        for i in range(self.size):
            self.dataList.append(SingleLinkList())

    def addNode(self, indexOne, indexTwo):
        pass


if __name__ == '__main__':
    pass



#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
- 怎样理解堆和栈？
- 数据结构中的堆和栈：
    - 堆：一种特殊的树结构，是一颗完全二叉树，在排序中有大顶堆、小顶堆概念。
    - 栈：先进后出或后进先出的一种结构，顺序栈（很少用，涉及到动态扩容问题）、链式栈
- 物理内存
    逻辑上分为：代码区、静态区、动态区
    - 代码区：存放代码的二进制表示。
    - 静态区：存放全局变量、常量、静态变量
    - 动态区：
        - 栈：
            - 形参、局部变量、函数返回值
        - 堆：
            - 创建出来的对象放在堆区

- 表达式求值问题？
    用两个栈实现，一个放数据，另一个放运算符，当当前运算符的优先级大于栈顶运算符优先级的时候，将运算符压入栈
    中，反之弹出栈顶运算符进行计算，从数据栈顶依次取出两个个数据，依次作为右操作数和左操作数进行计算，将计算
    结果压入数据栈中，直到运算符优先级大于栈顶运算符优先级为止，最后清空运算符栈进行如上计算，获得结果。

- 括号匹配问题？
    用一个栈实现，将左括号入栈，当遇到右括号的时候出栈并比较是否是对应的左括号，如果不是则不匹配，如果是继续
    进行，知道字符串结束，检查栈是否为空，为空该字符串括号匹配没有问题，如果不为空，则括号匹配有问题。

- 浏览器前进后退功能怎么实现？
    用两个栈进行实现，前进分配一个栈，后退分配一个栈。

- 函数调用利用栈来实现的
    函数调用中间状态的保存使用栈这种数据结构实现。

'''

from data_structure import SingleLinkList
import json


class Stack(): # 栈的链式实现
    def __init__(self):
        self.linkList = SingleLinkList()
        self.size = self.linkList.size

    def push(self, value):
        self.linkList.insertFisrt(value=value)
        self.size += 1

    def pop(self):
        tempNode = self.linkList.delFirst()
        self.size -= 1
        return tempNode

    def __str__(self):
        data = {
            'data': [],
            'size': self.size
        }
        tempNode = self.linkList.head.next
        if self.size == 0:
            return json.dumps(data)
        while (tempNode):
            data['data'].append(tempNode.data)
            tempNode = tempNode.next
        return json.dumps(data)


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    print(stack)
    print(stack.pop().data)
    print(stack)

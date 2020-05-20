#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time    : 2020/5/20 10:02 AM
# @Author  : fanding
# @FileName: register.py
# @Software: PyCharm
# @微信公众号: 樊樊家园


'''
通过装饰器向一个字典中添加数据，使用场景插件注册机制等等。
'''

plugins = {}


def register(plugin):
    plugins[plugin.__name__] = plugin
    return plugin


@register
# 上面装饰器等价于：transfer_age_to_int = register(transfer_age_to_int)
def transfer_age_to_int(doc):
    try:
        doc['age'] = int(doc['age'])
    except ValueError:
        doc['age'] = 'N/A'
    return doc


@register
# 上面装饰器等价于：filter_date = register(filter_date)
def filter_date(doc):
    date = doc['doc']
    if date < '2020-05-01':
        return None
    return doc


print(plugins)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 19:29
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 生成器.py

# 列表生成器
li = (x for x in range(20) if x % 2 == 0)
print(li)
print(type(li))     # generator类型
print(list(li))


# 函数生成器
def li_func():
    for x in range(20):
        if x % 2 == 0:
            yield x     # 返回生成器


print(li_func())
print(type(li_func()))  # generator类型
print(list(li_func()))


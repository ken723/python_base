#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 19:47
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 命名空间与作用域.py

# 在控制台使用
# globals()和locals()函数可以查看当前程序的所有全局和本地变量
s = 1000
n = 500


def sum_func(x):
    s = 0       # s是本地变量, 和函数外面的s没关系
    global n     # n是全局变量, 和函数外面的n是同一个
    s = x + n   # s = 10 + 500
    return s


print('s: ', s)
print('n: ', n)
print(sum_func(10))


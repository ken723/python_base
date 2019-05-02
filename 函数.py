#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 17:21
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 函数.py


# 默认值参数
# 默认值参数必须从后向前给出
def my_default_func(name='ken', age=22):
    print(name, '-', age)


my_default_func()


# 不定个数参数
def my_func(*args):
    print(args)
    print(type(args))


my_func(1, 2, 3)


# 不定个数 关键字参数
def my_func2(**kwargs):
    print(kwargs)
    print(type(kwargs))


my_func2(name='ken', age=23)





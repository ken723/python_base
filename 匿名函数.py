#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 19:09
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 匿名函数.py

# 下面的操作将列表中的元素首字母大写, 并加上'...'
name_li = ['ken', 'tom', 'jerry']


def str_func(s):
    # 将字符串首字母大写, 结尾加上'...'
    return s.title() + '...'


# 1. 通过str_func方法将列表中的名字处理
# new_li = [str_func(s) for s in name_li]
# print(new_li)


# 2. 通过map函数可以将函数应用到每一个元素上, 返回迭代器
# new_li = map(str_func, name_li)
# print(list(new_li))


# 3. 使用lambda表达式创建 匿名函数, 省略str_func方法.
# x 代表操作的对象
# ':'后面是对象需要的操作
new_li = map(lambda x: x.title() + '...', name_li)
print(list(new_li))







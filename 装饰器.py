#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 20:49
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 装饰器.py

# 在不改变原有函数代码的情况下, 为函数添加新的功能


def sum_func_doc(func):
    def inner_func(*args):  # 在装饰器内部的函数中处理func以及传进来的参数
        print('name: ', func.__name__)
        print('doc : ', func.__doc__)
        return func     # 返回处理后的func
    return inner_func   # 返回装饰器的处理函数


def sum_func_double(func):
    def inner_func(*args):
        n = args[0]
        print(n)
        return func
    return inner_func


# @sum_func_double
@sum_func_doc
def sum_func(a, b):
    '''
    计算a+b的和
    :param a:
    :param b:
    :return:
    '''
    return a + b


# 将参数和函数地址一同传入装饰器中的处理函数inner_func.
# 这里传入的参数需要和装饰器中的处理函数保持匹配
sum_func(10, 20)




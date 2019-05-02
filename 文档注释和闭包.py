#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 17:56
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 文档注释和闭包.py


# 文档注释
# 在控制台可以使用help(my_func)或my_func.__doc__查看
def my_func(x, y):
    '''
    求x与y的和
    :param x:
    :param y:
    :return:
    '''
    print('x: ', x)
    print('y: ', y)

    return x ** y


my_func(10, 20)


# 闭包
# 使用同一个函数动态生成不同的函数操作
def my_func_2(num):
    def inner(x):
        return x ** num
    return inner


func = my_func_2(2)     # 生成函数 计算x的2次方
print(func(3))          # x: 3

func = my_func_2(3)     # 计算x的3次方
print(func(3))          # x: 3

func = my_func_2(4)     # 计算x的4次方
print(func(2))          # x: 2




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 22:52
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 模块.py

# 导入模块
import 测试模块  # 导入一个模块
import 测试模块 as Test  # 为导入的模块取一个别名
from 测试模块 import sum_func   # 从模块导入一个函数
from 测试模块 import sum_func as sf  # 为导入的函数取一个别名

a = 测试模块.sum_func(0, 1)
print(a)

a = Test.sum_func(10, 20)
print(a)

b = sum_func(1, 2)
print(b)

c = sf(3, 4)
print(c)


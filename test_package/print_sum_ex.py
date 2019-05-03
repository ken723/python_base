#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 9:23
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : print_sum_ex.py

# 引用其他模块, 需要指定包名, 即使是在同一个包内.
# 只有在当前工作目录python_base内可以直接引用其他模块
from test_package import print_sum

a = print_sum.sum_func(1, 2)
print(a)


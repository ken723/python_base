#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 23:39
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 文件与包的组织.py

# 默认情况下, import语句从当前目录搜索模块
# sys.path中记录了搜索的系统路径
# 当文件夹中写有__init__.py文件时, 文件夹成为包

import sys  # 导入系统路径下的模块
from test_package import print_sum  # 导入自定义包的模块

print('sys.path: ')
for i in sys.path:
    print(i)

print(sys.argv)

a = print_sum.sum_func(1, 2)
print(a)







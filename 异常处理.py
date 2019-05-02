#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 22:24
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 异常处理.py

a_list = [1, 2, 3, 4, 5]
position = 9
# position = 'fds'

try:
    print(a_list[position])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)



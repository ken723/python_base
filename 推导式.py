#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 16:43
# @Author  : Ken
# @Email   : wqhken723@sina.com
# @File    : 推导式.py

# 列表推导式
int_li = []
for i in range(5):
    int_li.append(i)
print(int_li)

# 使用列表推导式
new_int_li = [i for i in range(10)]
print(new_int_li)

# 加入判断条件
new_int_li = [i for i in range(10) if i % 2 == 0]  # 偶数
print(new_int_li)

# 例如: 使每一个名字首字母大写
name_li = ['ken', 'tom', 'jerry']
new_name_li = [name.title() for name in name_li]
print(new_name_li)


# 字典推导式
# 名字作为key, 名字的长度作为value
stu_dict = {name: len(name) for name in name_li}
print(stu_dict)


# 集合推导式
# 名字长度大于3的构成集合
stu_set = {name for name in name_li if len(name) > 3}
print(stu_set)


# 生成器
# 只能运行一次
s = (x*x for x in range(20) if x*x > 50)    # ()是生成器类型
print(list(s))  # 生成器通过list()可以看到元素值, 否则是地址




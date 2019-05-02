# dict
# 字典是无序的, key唯一

# 创建
a = {'a': 1, 'b': 2, 'c': 3}
print("a: ", a)
b = dict(['x0', 'y9'])
print("b: ", b)

# 取值
print(a['c'])       # 如果'c'不存在, 报错KeyError
print(a.get('d'))   # 如果'd'不存在, 返回None
print(a.get('f', 0))   # 如果'f'不存在, 返回0

# 添加元素
a['d'] = 4
print(a)

# 修改元素
a['b'] = 20
print(a)

# 合并
# 字典不支持 '+' 合并
a.update(b)     # 修改了a的值
print(a)

# 删除元素
del a['d']
print(a)

# 清除元素(不常用)
# a.clear()
# print(a)

# 判断某个key是否在字典中, 返回bool
x = 'c' in a
print(x)


print()
# 返回所有key, 返回迭代器
print(a.keys())
print(list(a.keys()))   # 迭代器转list

# 返回所有values, 返回迭代器
print(list(a.values()))

# 返回所有键值对, 返回迭代器
print(list(a.items()))




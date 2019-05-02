# if else
if 1:
    pass
else:
    pass

# 遍历次数控制range()
for i in range(3):
    print(i, end=' ')
print()

print(list(range(1, 20, 2)))    # 开始, 结束, 步长
print()

# 遍历字典
a = {'a': 1, 'b': 2, 'c': 3}

# 遍历key
for key in a.keys():
    print(key, end=' ')
print()

# 遍历value
for val in a.values():
    print(val, end=' ')
print()

# 同时遍历key和value
for key, val in a.items():
    print(key, '', val)
print()

# zip()对两个或以上的容器进行迭代
# 迭代器通过list()转换为列表, 元素是元组类型
name_li = ['ken', 'tom', 'jerry']
age_li = [12, 23, 31]
id_li = ['001', '002', '003']

# 使用zip()迭代3个列表, 解包给name,age,uid
for name, age, uid in zip(name_li, age_li, id_li):
    print(name, '-', age, '-', uid)








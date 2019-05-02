# tuple
# 元组的元素值不能修改

# 创建元组
a = (1, 2, 3)
print(a)
b = 1, 2, 3
print(b)

# 只有一个元素时, 元素后面必须加 ','
c = (1)         # 错误写法
print(1)
print(type(c))  # c是int类型

c = (1,)        # 正确写法
print(c)
print(type(c))  # c是tuple类型

# 元组解包
x, y, z = a
print(x, y, z)

# 交换两个数的值
x, y = y, x
print("x: ", x)
print("y: ", y)

# 列表转元组
l = [4, 5, 6]
a = tuple(l)
print(a)

# 字典转元组
d = {'a': 1, 'b': 2, 'c': 3}
a = tuple(d)
print(a)


# set 集合
# 结合就是只有key的字典
# 集合的元素时无序, 唯一的
# 利用set的唯一性, 可以去重

# 创建集合
a = {'a', 'b', 'c'}
print(a)
b = set(['a', 'b', 'c'])
print(b)

# 利用set的唯一性去重
num_list = [1, 2, 3, 4, 4, 3, 2, 5]
a = set(num_list)
print(a)

# 判断元素是否在集合中, 返回bool
print(3 in a)
print(10 in a)

# 添加元素
a.update({11, 22, 33})
print(a)

# '\'连接多行代码
s = "fdsjfdklfj\
fdsfsfds"
print(s)









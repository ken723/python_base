# list
a = ['ken', 'tom', 'wong', 22, 34, 25]
b = list('hello world')

print(a)
print(b)

# 切片 [开始:结束:步长]
print(a[0:2])
print(a[0:4:2])
print(a[:5:3])
print(a[::-1])  # 步长-1代表反转(逆序)

# 赋值
a[0] = 'jerry'  # 赋值一个
a[1:3] = ['t', 'w']     # 赋值多个
print(a)

# 嵌套列表
a[1] = [1, 2, 3]
print(a)
print(a[1][-1])  # 先取a[1]的值, 再取a[1]的[-1]位置

# 列表合并
c = a + b
print("c: ", c)

# 列表扩充
a.extend(b)     # 将b合并入a, 修改了a的值
print("a: ", a)

# 追加元素
# 常用于在循环中为列表添加元素
b.append('append1')     # 在b末尾追加元素
print("b: ", b)

# 弹出元素
# 从列表尾部删除元素, 并返回该元素的值
x = b.pop()
print("b: ", b)
print("x: ", x)
# 也可以指定弹出某一个位置的元素
x = b.pop(0)
print("b: ", b)
print("x: ", x)

# 根据元素值删除元素
b.remove('e')
print("b: ", b)

# 在任意位置插入元素(不常用)
b.insert(0, 'x')
print("b: ", b)


# 判断列表是否包含某元素, 返回bool
x = 'o' in b
print("x: ", x)

# 列表排序
b = [5, 4, 4, 3, 99, 1, 0]
b.sort(reverse=True)    # 默认升序, reverse指定降序
print("b: ", b)

# 求列表中某元素出现的次数
n = b.count(4)
print("n: ", n)

# 求列表中某元素的位置
n = b.index(4)
print("n: ", n)

print("************************")


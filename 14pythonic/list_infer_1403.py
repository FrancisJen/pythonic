# 14-3 列表推导式：非常有python特色, 可以完成map完成的功能
# 14-4: dict如何编写列表推导式
a = [1,2,3,4]
# 如果加上顾虑条件，推荐用列表推导式，因为map实现的话需要结合filter一起比较复杂
b = [i**2 for i in a if i >= 3]
print(b)

# 同样可以用作其他数据类型，set，dict，tuple

a = {1,2,3,4}
b = {i**2 for i in a if i >= 3}
print(b)


# dict
students = {
    'francis': 18,
    'shirley': 20,
    'smile':4
    }
b = {k for k,v in students.items()}
print(b)

# tuple
a = (1,2,3,4)
# 不推荐用tuple，用list方便一些
b = (i**2 for i in a if i >= 3)
# tuple默认是generator，需要进行转换
print(list(b))



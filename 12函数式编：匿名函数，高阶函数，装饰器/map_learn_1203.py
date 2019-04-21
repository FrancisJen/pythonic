# 12-3 map
# 12-4 map和lambda

list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6]

def square(x):
    return x * x

r = map(square, list_x)

# map + lambda: 使用lambda替换square函数
# 注意lambda传入的参数有几个，后面的列表参数就要有几个，也就是x对应list_x, y对应list_y
# 计算的结果的个数和参数列表中个数最少的那个长度一样
r = map(lambda x,y: x*x+y, list_x, list_y)
print(list(r))




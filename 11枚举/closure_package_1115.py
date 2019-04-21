# 11-15 再用闭包解决一下
# pos是环境变量， 返回一个函数，这是必包的两个特征
origin = 0

def factory(pos):
    def go(step):
        nonlocal pos # or global origin
        new_pos = pos+step
        pos = new_pos
        return pos
    return go

tourist = factory(origin)

# 闭包有保存现场的功能，记住了上次调用的状态
print(tourist(2))
# 闭包的变量作用在函数内部，并不会改变全局变量
# print(origin)
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
# 闭包记住了上次的状态
print(tourist.__closure__[0].cell_contents)
print(tourist(4))
print(tourist.__closure__[0].cell_contents)

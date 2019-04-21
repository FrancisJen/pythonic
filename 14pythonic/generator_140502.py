# 生成器
# print 0-10000
    
    
# list是进行了存储，消耗了内存
'''
n = [i for i in range(0,10001)]
for i in n:
    print(i)
'''

# 列表推导式可以作为生成器
n = (i for i in range(0,10001))
print(next(n))
print(next(n))


# 不存储的方式，
def gen(max):
    n = 0
    while n < max:
        # 但是我不一定想print，只是想让你返回0-10000，我来去运用
        # print(n)
        n += 1
        # 但是直接return这个循环就退出了
        # return n

        yield n  #****第一次调用next的时候返回n，但是不退出循环，第二次调用next会接着第一次返回的地方继续执行

# 这就是生成器
g =  gen(10000)
# 生成器可以被next调用，也可以通过for循环遍历
'''
print(next(g))
print(next(g))
print(next(g))
'''

# for i in g:
#     print(i)

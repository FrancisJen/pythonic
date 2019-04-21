# 14-8 装饰器的副作用

import time
from functools import wraps

def decorator(func):
    # 装饰器导致f1不能保留原来的函数名, 也不能查看该函数的帮助文档：
        #下面这个装饰器可以解决这个问题
    @wraps(func)  #wraps将func的信息复制到wrapper中，这样wrapper就知道了f1这个函数信息
    def wrapper():
        print(time.time())
        func()
    return wrapper

"""
def f1():
    '''
        this is decription of f1 function
    '''
    print(f1.__name__)
f1()   #结果是f1
print(help(f1)) # 打印说明of f1
"""

@decorator
def f2():
    '''
        this is decription of f2 function
    '''
    print(f2.__name__)
f2()   #结果是wrapper...
print(help(f2))  # 加了装饰器之后不会打印说明of f2



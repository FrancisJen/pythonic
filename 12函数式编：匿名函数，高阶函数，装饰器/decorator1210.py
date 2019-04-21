import time

def decorator(func): 
    def wrapper(*args, **kwargs):
        print_time()
        func(*args, **kwargs)
    return wrapper

def print_time():
    print(time.time())

@decorator
def f1(name, address):
    print('this is a function, name:' + name )
    print('this is a function, adress:' + address )

@decorator
def f2(name, address, **kwargs):
    print('this is a function, name:' + name )
    print('this is a function, adress:' + address )
    print(kwargs)


f1('francis', 'Thailand')
f2('francis', 'Thailand', role='飞行员', age=30)

# 了解下AOP思想
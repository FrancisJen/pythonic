# 14-8 __len__ and __bool__内置方法

# class内部没有内置方法的时候，默认bool返回为False
class Test():

    # 当内置方法包涵len和bool两个的时候，bool(实例对象) 返回以__bool__定义的为准
    def __bool__(self):
        return False # only return Bool
    def __len__(self):
        return 1  # return int or Bool

test = Test()
# len和bool都会触发对内置方法的调用__len__
print(len(test))
print(bool(test)) 


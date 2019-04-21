# 14-7 对象存在不一定是True

class Test():
    def __len__(self):
        return 0
    def __bool__(self):
        return False


test = Test()
print(bool(test))


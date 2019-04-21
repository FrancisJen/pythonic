# 0912: 成员可见性：公开和私有
# 通过方法对成员变量赋值

class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.__score = 0

    # 私有方法
    def marking(self, score):
        if score < 0:
            print('score is invalid')
        else:
            self.__score = score
        print(self.__score)

student1 = Student('shirley',22)
# 私有属性不是可以被访问和更新值，而是添加了一个新的属性
student1.__score = 33
print(student1.__score)
print(student1.__dict__)
# {'name': 'shirley', 'age': 22, '_Student__score': 0, '__score': 33}

# 这个才是真的访问私有变量，结果不可访问
student2 = Student('shirley',22)
# print(student2.__score)
print(student2.__dict__)
# {'name': 'shirley', 'age': 22, '_Student__score': 0}
# student1.marking(44)

# 区别student1和student2的变量，发现__score是后来增加的一个变量


# 但是私有变量可以被间接访问
print(student2._Student__score)
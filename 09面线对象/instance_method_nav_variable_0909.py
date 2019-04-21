# 在实例方法中访问实例变量和类变量
class Student():
    sum = 0
    name = 'francis'
    age = 18

    def __init__(self, name, age):
        # 构造函数，初始化对象的属性
        self.name = name 
        self.age = age

        print(self.age) #访问实例变量
        print(self.__dict__) #在构造函数中打印所有的实例变量

        print(Student.name) #在实例方法中使用类变量
        print(self.__class__.name) #通过self访问类变量

    def all(self):
        print(self.__dict__) #在实例方法中打印所有的实例变量


student1 = Student('shirley', 18)
student1.all()
print(Student.name) #在外部访问类变量
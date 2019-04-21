# 0914 继承
# 0915 字类中调用父类方法，super关键字

class Human():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('parent english homework')

class Student(Human):
    # 子类和父类的构造函数参数不一致
        # 需要把父类的参数放进去
    def __init__(self, school, name, age):
        self.school = school
        # 在子类中调用父类的构造函数来传递参数给父类并进行初始化
        # 这里需要传入self：类调用实例方法，需要传入self，当父类名字变化的时候这里需要重写
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)


    # 子类和父类同名，优先调用子类的方法
    def do_homework(self):
        # 子类的方法中调用父类的方法
        super(Student, self).do_homework()
        print('english homework')
 

# 实例变量（构造函数）也可以被继承，需要在子类实例化的时候声明
student1 = Student('实验小学', 'francis', 77)
print(student1.sum)
# 子类继承父类的类变量Student.sum
# print(Student.sum)
print(student1.name) 
print(student1.age)

# 实例方法也可以被继承
# student1.get_name()

student1.do_homework()

# 在实例方法中访问实例变量和类变量
class Student():
    sum = 0
    # name = 'francis'
    # age = 18

    def __init__(self, name, age):
        # 构造函数，初始化对象的属性
        self.name = name 
        self.age = age

        # self.__class__.sum += 1
        # print('当前班级人数为:' + str(self.__class__.sum))

    def do_homework(self):
        # 在实例方法中操作类变量
        self.__class__.sum += 1
        print('当前班级人数为:' + str(self.__class__.sum))
        print('homework')

    # 定义类方法， 主要用来操作类变量，将sum＋1的操作在类方法中实现会更简单
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级人数为:' + str(cls.sum))



student1 = Student('francis',18)
# student1.do_homework()
# 用类调用类方法
Student.plus_sum()  
# 实例对象也可以调用类方法, 个人建议不要这样用，说不通
student1.plus_sum()
student2 = Student('shirley',18)
# student2.do_homework()
Student.plus_sum()
student3 = Student('natume',1)
# student3.do_homework()
Student.plus_sum()




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
        # self.__class__.sum += 1
        # print('当前班级人数为:' + str(self.__class__.sum))
        print('homework')

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级人数为:' + str(cls.sum))

    # 静态方法可以用类方法来代替，而且调用类变量更方便，这个方法和对象的关系很弱，不建议使用
    # 当这个和类，对象没有什么关系的时候可以用，不过不推荐
    # 静态方法不可以访问实例变量
    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('this is a static method!')

student1 = Student('francis', 18)
student1.add(1,2)
Student.add(1,2)




day = 11

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'
    
def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknown'    

switcher = { 
    0: get_sunday,
    1: get_monday,
    2: get_tuesday,
}

# 和switcher[day]的区别是， 当day不存在时，get不会报错而是返回一个默认值
# return一个方法，后面加()才能调用
day_name = switcher.get(day, get_default)()
print(day_name)
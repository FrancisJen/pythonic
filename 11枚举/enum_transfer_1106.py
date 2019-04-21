# 11-5 枚举注意事项
from enum import Enum

class VIP(Enum):
    # 两个枚举类型的value一样，第二个就是第一个的别名，也就是打印VIP.GREEN == VIP.YELLO
    YELLOW = 1  
    # GREEN = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

a = 1
print(VIP(a))

if a == VIP.YELLOW:
    pass
elif a == VIP.BLACK:
    pass
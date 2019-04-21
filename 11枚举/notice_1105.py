# 11-5 枚举注意事项
from enum import Enum

class VIP(Enum):
    # 两个枚举类型的value一样，第二个就是第一个的别名，也就是打印VIP.GREEN == VIP.YELLO
    YELLOW = 1  
    # GREEN = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

# print(VIP.GREEN, type(VIP.GREEN))  #枚举类型

# # 遍历枚举类型,不会打印出别名
for v in VIP:
    print(v)

# 遍历枚举类型,打印出别名
for v in VIP.__members__.items():
    print(v)


# 遍历枚举类型,只打印出 标签名
for v in VIP.__members__:
    print(v)    
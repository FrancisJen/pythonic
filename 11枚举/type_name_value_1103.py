# 11-3 枚举类型，名称和值
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.GREEN, type(VIP.GREEN))  #枚举类型
print(VIP.GREEN.name, type(VIP.GREEN.name)) #str
print(VIP.GREEN.value)
print(VIP['GREEN'])  #通过名称获取枚举类型

# 遍历枚举类型
for v in VIP:
    print(v)
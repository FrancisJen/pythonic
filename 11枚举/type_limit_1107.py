# 11-6 枚举转换

from enum import Enum
from enum import IntEnum, unique  # value为int且唯一

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 2
    RED = 4 

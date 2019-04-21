# 10-3字符集

import re
s = 'abc, acc, adc, aec, afc, ahc'
# ［］里是或的关系
r = re.findall('a[cfd]c', s)
print(r)
# 非cfd的
r2 = re.findall('a[^cfd]c', s)
print(r2)

# 匹配c到f
r3 = re.findall('a[c-f]c', s)
print(r3)
# 非c-f
r4 = re.findall('a[^c-f]c', s)
print(r4)
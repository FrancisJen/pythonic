# 10-7:匹配0次1次或无限多次

# *匹配0或者无限多次
# +匹配1或者无限多次
# ?匹配0或者1次, 可以用作去重
import re
a = 'pytho0python1pythonn2'

# *左边的字符出现0或者无限多次
r1 = re.findall('python*', a)
r2 = re.findall('python+', a)
r3 = re.findall('python?', a)

# print(r1,r2,r3)

# 贪婪与非贪婪，默认是贪婪模式
r4 = re.findall('python{1,2}', a)
print(r4)
# ?就是非贪婪模式，只出现一次n就获取
r5 = re.findall('python{1,2}?', a)
print(r5)
from functools import reduce

# reduce连续计算，连续调用lambda, 上一次lambada的结果作为x再次传入lambda
list_x = [1,2,3,4,5,6,7,8]
r = reduce(lambda x,y: x+y, list_x)
print(r)
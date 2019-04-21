# 14-5: iterator, Generator

# 可迭代对象，iterable： list， tuple， set
    # for i in iterable
    # 可迭代对象不一定是迭代器：list
# iterator： 是对象也就是class, 也是可迭代对象
    # 如何将普通的对象变为可迭代对象呢
        # 包含 def __iter__(self) & def __next__(self)
    # 迭代器是一次性，遍历之后就不能再此遍历了
        # 如何遍历两次呢：
            # 遍历之前先copy这个对象
# diff:
    # 迭代器是可迭代对象，但是反之不一定
    # next方法只能用于迭代器
    # 迭代器是一次性，遍历之后就不能再此遍历了，但是list和tuple可以循环遍历   


class Book:
    pass

class BookCollection:
    def __init__(self):
        self.data = ['《往事》','《只能》','《回味》']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r

books = BookCollection()

import copy
books2 = copy.copy(books)
# print(next(books))
# print(next(books))
# print(next(books))

for book in books:
    print(book)
    
for book in books2:
    print(book)    
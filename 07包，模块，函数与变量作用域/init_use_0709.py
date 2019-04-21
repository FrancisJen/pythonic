# 指定同级目录下只有c7.py是可以被其他模块引用的
    # __all__ = ["c7"]


# 如何解决每个py文件都引用相同的库的问题
# 在t文件夹下放置__init__.py
# 每个py文件直接import t
# 例如： 
    # import t
    # print(t.sys.path)



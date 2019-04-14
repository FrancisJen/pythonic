list_x = [1,0,2,0,3,0,4,0]

r = filter(lambda x: True if x!=0 else False, list_x)
print(list(r))
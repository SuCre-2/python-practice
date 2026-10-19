# I2 ★｜迭代字典
# 用 for 循环遍历一个字典，同时拿到 key 和 value
# 提示：for k, v in d.items()

def f(**kwargs):
    L = []
    for k,v in kwargs.items():
        L.append(f'{k}={v}')
    return L

print(f(age =5,city = '上海'))

#不写函数的话
S ={'a':2,'b':8,'c':16,'d':4}
for x,y in S.items():
    print(f'{x}={y}')

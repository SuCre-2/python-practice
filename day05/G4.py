# G4 ★★｜关键字参数
# 写一个函数，接收任意个 键=值 参数，把它们打印成 key=value 的形式
# 提示：def f(**kwargs)，kwargs 是一个字典

#两个例子，值得琢磨
def g(**kwargs):
    l =[]
    for k, v in kwargs.items():
        l.append(f"{k}={v}")
    return l

print(g(age=4,city='北京',gender='女'))

def s(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}")
s(age=4, city='北京', gender='女')
s(a=1, b=2)
s()

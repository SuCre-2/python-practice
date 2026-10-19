# G3 ★｜不定长参数
# 写一个函数，接收任意个数字，返回它们的和
# 提示：def f(*args)，args 是一个元组

def f(*args):
    if not args:
        return 0
    for n in args:
        n += n
    return n

print(f(1,2,3))
print (f())
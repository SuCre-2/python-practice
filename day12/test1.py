# try 
try:
    print('tey...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('excep:t',e)
finally:
    print('finally...')
print('END')

# 在try块中，如果出错，后续代码不执行而是直接跳转到错误执行代码，也就是
# except语句块，如果有finally就继续执行（有finally一定执行不管错没错

# 于是上述代码会输出
# try...
# except: division by zero
# finally...
# END

#不同类型错误由不同的except语句块来捕获处理执行
#在except语句块的后面加入else，那么没错误就会执行else
#本节学习错误异常处理，如何看错误信息

#loogging可以记录错误信息然后继续继续执行程序
#在python错误也是class，捕获一个错误就是捕获到class的一个实例
#可以自己定义一个错误然后用raise抛出

from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main() #分析错误
# 100 + 200 + 345 = 645
# Traceback (most recent call last):
#   File "C:\Users\SuCre\code\day12\test1.py", line 45, in <module>
#     main()
#   File "C:\Users\SuCre\code\day12\test1.py", line 42, in main
#     r = calc('99 + 88 + 7.6')
#         ^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\SuCre\code\day12\test1.py", line 37, in calc
#     return reduce(lambda acc, x: acc + x, ns)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\SuCre\code\day12\test1.py", line 32, in str2num
#     return int(s)
#            ^^^^^^
# ValueError: invalid literal for int() with base 10: ' 7.6'

#45行错误，指向42，指向37，指向32，发现7.6不是int类型，无法解析，
# 抛出错误是 ValueError，指向str2num()，修复思路是让函数根据输入转换类型
# 可以判断字符串是否有小数点来转换

# def str2num1(s):
#     s = s.strip()    #去掉首位空格
#     if '.' in s:
#         return float(s)
#     return int(s)

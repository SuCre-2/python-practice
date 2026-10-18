# def my_abs(x):
#     if x>= 0:
#         return x
#     else :
#         return -x

# print (my_abs(-98))

#from 文件名 import 函数名
#可以调用当前文件夹已经定义的函数

#pass可以当作占位符，先让代码运行起来

#函数参数检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

#函数返回多个值时，其实是返回一个tuple，语法上返回tuple可以省略括号
#题目：定义函数quadratic (),接受三个参数，返回一元二次方程a（x）平方+bX+c=0的两个解

import math

def quadratic(a,b,c):
    delta = b*b - 4*a*c          # 先算判别式
    if delta < 0:
        return None              # 没有实数根，返回 None
    
    x1 = ((-b)+(math.sqrt(b*b-4*a*c)))/(2*a)
    x2 = ((-b)-(math.sqrt(b*b-4*a*c)))/(2*a)
    return x1,x2

a= int(input("输入a:"))
b= int(input("输入b:"))
c= int(input("输入c:"))

y=quadratic(a,b,c)
if y is None:
    print("无实数根")
else:
    x1,x2=quadratic(a,b,c)
    print(x1,x2)
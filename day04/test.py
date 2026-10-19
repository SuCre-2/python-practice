# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def mul(x,*y):  #x收入第一个实参，然后把剩下的打包进*y
    r = x       #累积变量
    for n in y: #y可能空也可能不空，如果不空放入n
        r *= n  #此写法等价于r = r*n，如何循环到y空
    return r    #这样一来，把校验工作交给ptyhon，不用多写一段判断，如果没传入一个参数，函数直接报错

# # 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
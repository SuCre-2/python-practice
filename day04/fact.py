#递归
# def fact(n):
#     if n ==1:
#        return 1
#     return n*fact(n - 1)

# print(fact(1))

# print(fact(2))

#print(fact(5))
#展开：
#fact(5)-->5*fact(4)-->5*4*3*2*1
#fact(4)-->4*fact(3)
#...
#fact(1)-->1

# print(fact(10))

# print(fact(2000)) #要注意防止栈溢出

#函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出

#尾递归解决问题：和循环效果一样
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#改：
# def fact(n):
#     return fact_iter(n,1)

# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num * product)
#没看懂说实话，fact调用了fact_iter，这样fact不会溢出
#那fact_iter呢？，他负责计算，他溢出了怎么办？
#python没有尾递归，所以用不了
#但可以循环实现优化：
def fact(n):
    r = 1
    for i in range(2, n + 1):  #复习range()，从2开始生成到n+1，不包括n+1
        r *= i                 #r = r*i,思路是先赋值r=1,然后循环生成2到n的数字赋值给i，然后拿r去乘.
    return r                   #得到阶乘结果

#循环不会栈溢出，用循环代替递归防止溢出

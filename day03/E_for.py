#循环
#for ... in

name = ['miky','bob','tibo']

for N in name:
    print(N)

#创造一个新变量N，取出依次代入变量N然后执行缩进块的语句
#利用range()和for ...in可以完成计算1到任意大的数字的整数和

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# for x in range(1001):
#     sum = sum + x
# print(sum)

#2是while循环，满足条件一直循环，不满足就退出
#计算100以内的奇数之和
# 可以用两个计数器，一个0，一个99
# 让0去累加，99去递减，如下：
sum = 0
n = 99
while n > 0:
    sum = sum + n    #0+99+97+95+...
    n = n - 2
print(sum)

L=['Bart','Lily','Adam']

for x in L:
    print(f'Hello,{x}')

#一般参与反复赋值的变量不会在后续产生影响，除非你改变了赋值还用同一用途
#但是参与循环以后的变量要小心，+运算后创建新的对象但是+=后是原地改，也就是多个变量指向的这一个对象都会改变

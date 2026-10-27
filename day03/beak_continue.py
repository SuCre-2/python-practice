# break用来提前退出循环

# continue则是跳过后续操作
# 也就是提前结束本轮，直接开始下一轮循环

n = 0
while n < 10:
    n=n+1
    if n%2==0:
        continue
    print(n)
#一个很妙的嵌套，让程序只输出奇数，偶数就直接跳过

# 本次请写出一个死循环

# n = 0
# while n < 50:
#     n = n + 1
#     print(n)
#     x = n - 1
#     print(x)
#     n = x
#     print(n,x)


    
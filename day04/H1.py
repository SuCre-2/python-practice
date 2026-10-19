#用递归和循环各写一遍阶乘factorial(n)

def fact_rec(n):
    if n == 1 or n ==0:
        return 1
    return n*fact_rec(n-1)

print(fact_rec(0))
print(fact_rec(1))
print(fact_rec(5))

def fact_loop(n):
    r = 1
    for i in range(2,n+1):
        r *= i
    return r

print(fact_loop(0))
print(fact_loop(1))
print(fact_loop(5))

#晚上再练一遍
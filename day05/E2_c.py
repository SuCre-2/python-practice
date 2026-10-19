#重构E2成为函数：
#条件判断
def f():
    while True:
        s = input('请输入 0-100 的分数: ')
        if not s.isdigit():   
            print('输入不合法，请重新输入！')         # 是纯数字吗
            continue
        n=int(s)
        if 0 <= n <= 100:      # 范围对吗
            return n
        print('超出范围重新输入')              # 都对了 → 跳出循环

n = f()

def E(n):
    if n >= 90:
       return("A")
    elif n>=80:
       return("B")
    elif n>=70:
       return("C")
    elif n>=60:
       return("D")
    else:
       return("E")
    

#match

def G(n):
    match n:
        case y if y>=90:
          return("A")
        case y if y>=80:
          return("B")
        case y if y>=70:
          return("C")
        case y if y>=60:
          return("D")
        case _:
          return("E")

print("if/elif 评级:", E(n))
print("match 评级:  ", G(n))


# 函数() 只 return，不 print	一旦它 print，就没法在别处复用它。
# 专门一个函数负责"拿到合法分数"，不负责分级	一个函数只做一件事

# 改完能直接 print(grade(85)) 输出 B	这就是"函数能单独测试"的定义
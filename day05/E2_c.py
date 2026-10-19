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
#重点在于循环语句控制用户输入
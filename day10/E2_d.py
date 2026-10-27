#重构E2_c,装进一个类：
class Score:
    def __init__(self):
        self.n = self.is_pass()

    def is_pass(self):
        while True:
            s = input('请输入 0-100 的分数: ')
            if not s.isdigit():   
                print('输入不合法，请重新输入！')         # 是纯数字吗
                continue
            n=int(s)
            if 0 <= n <= 100:      # 范围对吗
                return n
            print('超出范围重新输入')              # 都对了 → 跳出循环

    def E(self):
        if self.n >= 90:
           return("A")
        elif self.n>=80:
           return("B")
        elif self.n>=70:
           return("C")
        elif self.n>=60:
           return("D")
        else:
           return("E")
        
    def G(self):
        match self.n:
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


S = Score()
print("if/elif 评级:", S.E())
print("match 评级:  ", S.G())
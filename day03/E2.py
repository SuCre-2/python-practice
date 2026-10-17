#条件判断

while True:
    s = input('请输入 0-100 的分数: ')
    if s.isdigit():            # 是纯数字吗
        n = int(s)
        if 0 <= n <= 100:      # 范围对吗
            break              # 都对了 → 跳出循环
    print('输入不合法，请重新输入！')

# if n >= 90:
#     print("A")
# elif n>=80:
#     print("B")
# elif n>=70:
#     print("C")
# elif n>=60:
#     print("D")
# else:
#     print("E")

#match

match n:
    case y if y>=90:
        print("A")
    case y if y>=80:
        print("B")
    case y if y>=70:
        print("C")
    case y if y>=60:
        print("D")
    case _:
        print("E")

#重点在于循环语句控制用户输入
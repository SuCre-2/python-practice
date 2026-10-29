#J1用 try/except 包裹 10 / 0，捕获 ZeroDivisionError 后输出友好提示
try:
    r = 10/0
except ZeroDivisionError as e:
    print('分母不能0')

#J2让用户输入一个数字，如果输入的不是数字（如 abc），捕获 ValueError 并提示重新输入
def f(s):
    return int(s)

while True:
    s = input("请输入一个数字: ")
    try:
        n = f(s)
    except ValueError:
        print("这不是数字，请重新输入")
    else:
        print(f"输入正确：{n}")
        break
    finally:
        print('?')
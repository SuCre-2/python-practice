class MyError(Exception):
    pass


def check(n):
    if n < 0:
        raise MyError('不能是负数')
    return n                     # 返回 n


while True:
    try:
        n = int(input("输入正整数:"))   # 转换在 try 内 → ValueError 抓得到
        s = check(n)                   # 传进去的已经是 int
    except MyError as e:
        print('捕获负数: ', e)
    except ValueError as e:
        print('捕获非整数: ', e)
    else:
        print('输入正确: ', s)
        break

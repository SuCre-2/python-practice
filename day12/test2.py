def div(a,b):
    try:
        r=a/b
    except ZeroDivisionError as e:
        print('分母不能0', e)
    else:
        print('没出错 结果是', r)
    finally:
        print('无论对错执行')
    return None

print(div(10,2))
print(div(10,0))


class MyError(Exception):
    pass

def check(n):
    if n<0:
        raise MyError('不能是负数')
    return 0

try:
    check(-1)
except MyError as e:
    print('捕获：', e)

print(check(2))
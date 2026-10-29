class InvalidOperatorError(Exception):
    pass

def f(a,b,op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError('除数不能为 0')
            return a / b
        case _:
            raise InvalidOperatorError(f'不支持的运算符 {op!r}')

def main():
    while True:
        print('——分隔——\n')
        op = input('运算符（ +、 -、 *、 / , q退出): ').strip()
        if op in ('q','Q'):
            print('已退出')
            return

        try:
            if op not in ('+','-','*','/'):
                raise InvalidOperatorError(f'不支持的运算符{op!r}')
            a = float(input('第一个数：'))
            b = float(input('第二个数：'))
            r = f(a,b,op)
        except ValueError:
            print ('输入的不是数字')
        except ZeroDivisionError as e:
            print(e)
        except InvalidOperatorError as e:
            print(e)
        else:
            print(f'{a} {op} {b} = {r}')


main()
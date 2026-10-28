# map,接受两个参数，一个函数一个iterable
# 传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
     return x * x

r = map(f, [1, 2, 3, 4, 5, 6])

print(list(r))

# reduce,接受两个参数，一个函数一个序列，
# reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))

# 练习：利用map()函数，
# 把用户输入的不规范的英文名字，
# 变为首字母大写，
# 其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()

map_result = map(normalize, ['adam', 'LISA', 'barT'])
print(list(map_result))

# 练习：利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def fn(x, y):
        return x * 10 + y

    # 分离整数部分和小数部分
    if '.' in s:
        integer_part, decimal_part = s.split('.')
        # 转换整数部分
        integer_value = reduce(fn, map(char2num, integer_part))
        # 转换小数部分
        decimal_value = reduce(fn, map(char2num, decimal_part)) / (10 ** len(decimal_part))
        return integer_value + decimal_value
    else:
        # 如果没有小数点，直接转换为整数
        return reduce(fn, map(char2num, s))
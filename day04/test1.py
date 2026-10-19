#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while len(s) >0 and s[0] == " ":    #如果字长>0 且开头是空格，切空格以后
        s = s[1:]
    while len(s)> 0 and s[-1] ==' ':    #如果字长>0 且结尾是空格，切空格以前
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
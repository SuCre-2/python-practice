#条件判断，针对某个变量匹配若干情况时，可以用match...case结构代替

score ='B'

if score == 'A':
    print('score:A')
elif score =='B':
    print('score:B')
elif score =='C':
    print('score:C')
else:
    print('None')

#以上结构等价于下

score ='A'
match score:
    case 'A':
        print('A')
    case 'B':
        print('B')
    case 'C':
        print('C')
    case _:    #表示任意值，仅能在最后
        print('None')
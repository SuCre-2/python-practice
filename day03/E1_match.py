#此学习match的复杂匹配

age = int(input('输入不为负的年龄：'))
match age:
    case x if x < 10:  #当age<10成立时，发生匹配，赋值给变量x
        print(f' < 10 years old : {x}')
    case 10:
        print('10 years old')
    case 11|12|13|14|15|16|17|18:
        print('11~18 years old')
    case _:
        print(f'> 18 years old : {age}')

#以上展示灵活的复杂匹配
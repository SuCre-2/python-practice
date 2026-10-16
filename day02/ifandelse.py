height = float(input("请输入身高："))
weight = float(input("请输入体重："))

BMI=weight/(height*height)

if BMI >=32:
    print(f'BMI为{BMI:.2f},严重肥胖')
elif BMI>=28:
    print(f'BMI为{BMI:.2f},肥胖')
elif BMI>=25:
    print(f'BMI为{BMI:.2f},过重')
elif BMI>=18.5:
    print(f'BMI为{BMI:.2f},正常')
else :
    print(f'BMI为{BMI:.2f},过瘦')
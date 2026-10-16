# B5 = "上海自来水来自海上"
# B5c = B5[::-1]
# print(B5,B5c)

# if B5 == B5c:
#     print(True)
B5 =input("请输入回文进行判断")
B5c = B5[::-1]
if B5 ==B5c:
    print(True)
else:
    print(False)

#不用if，直接比较运算的结果就是一个布尔值
#print (B5 == B5c)

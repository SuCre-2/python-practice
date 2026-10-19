#列表生成器
#生成列表可以list（range（1，11））
#生成1-10的列表

#但是列表里面的元素是变量怎么办
#循环
# L = []
# for x in range(1,11):
#     L.append( x * x )    #把x*x值放入L
# print(L)

#而列表生成式可以一行语句代替：

L=[x*x for x in range(1,11)]
print(L)

#把要生成的元素放在前面，跟上for循环就行
#加上判断语句还可以筛选出特定的值

P= [x * x for x in range(1, 11) if x % 2 == 0]
print(P)

#还可以用两层循环生成全排列

LP = [ m+n for m in 'ABC' for n in 'XYZ']
print(LP)

#，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# import os # 导入os模块，模块的概念后面讲到
# [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']

#因为for循环可以用两个到多个变量，所以也可以使用两个变量来生列表

d = {'x':'A','y':'B','z':'C'}
D=[k + '=' + v for k,v in d.items()]

print(D)
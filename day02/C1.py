#list的增删改查和遍历
#知识前览：
#l = ["a","b","c","d"]

#.append(),插入
#.insert(索引,),指定位置插入
#删除则是.pop()，默认删最后一个,指定位置.pop(i)
#删除还有remove(n)是删值：n，从左到右第一个n

#替换直接对着下标位置去赋值就行
#索引也就是下标

#查索引和值如下
#for x in l:
#    print(x)    #只查了值

#for i,x in enumerate(l):
#    print(i,x)    #同时下标和值
#内置函数把列表包装成下标，元素的形式成对发出

#for i in range(len(l)):
#    print(i,l[i])    #按照下标遍历
#range(n)为生成0到n-1的数
#然后l[i]就是用下表取值

C1= ["apple","banana"]
print(C1)

C1.append("orange")
print(C1)

C1.pop(0)
print(C1)

C1[0]="BANANA"
print(C1)
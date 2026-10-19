# I3 ★｜列表生成式
# 用一行代码生成 1 到 10 的平方列表 [1, 4, 9, ..., 100]

# I4 ★｜带条件的生成式
# 用一行代码生成 1 到 20 之间所有偶数
l=[x*x for x in range(1,11)]
print(l)
s=[x for x in range(1,21) if x%2==0]
print(s)
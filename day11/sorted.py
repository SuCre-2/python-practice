# sorted()函数用于对序列进行排序。
# sorted()也接收一个函数和一个序列。
# sorted()返回的是一个新列表，不会修改原序列。

# 示例：对一个数字列表进行排序
print(sorted([36, 5, -12, 9, -21]))
# 结果: [-21, -12, 5, 9, 36]

# 示例：对一个字符串列表进行排序，默认是按ASCII码大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 结果: ['Credit', 'Zoo', 'about', 'bob']

# 示例：对一个字符串列表进行排序，不区分大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 结果: ['about', 'bob', 'Credit', 'Zoo']

# 示例：对一个字符串列表进行排序，按长度排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=len))
# 结果: ['Zoo', 'bob', 'about', 'Credit']

# 示例：对一个数字列表进行降序排序
print(sorted([36, 5, -12, 9, -21], reverse=True))
# 结果: [36, 9, 5, -12, -21]

# 练习：假设用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)
# 请用sorted()对上述列表分别按成绩从高到低排序：
def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score, reverse=True)
print(L3)
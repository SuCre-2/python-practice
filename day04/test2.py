# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if not L:
        return(None,None)  #空序列保护
    
    min_x = max_x =L[0]    #暂时赋值，首元素初始化

    for x in L:
        if x < min_x:      
            min_x = x
        if x > max_x:
            max_x = x
    return (min_x,max_x)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
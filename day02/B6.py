# B6 = "上海自来水来自海上"
# B6c = B6[::-1]

# print(B6c)

#重复B5?
#关于reverse()如下
B6s = [1,2,3,4,'z']
B6s.reverse()

print(B6s)
#发现直接改变了列表，并不返回新列表，list专用
#B6q=B6s.reverse()的写法，使得B6q返回的是空值none
B6q=B6s.reverse()
print(B6q)
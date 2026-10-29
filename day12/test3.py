f = open('C:/Users/SuCre/code/day12/t.txt', 'r')

print(f.read())

f.close()

try:
    f = open('C:/Users/SuCre/code/day12/t.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#完全等价于：
with open('C:/Users/SuCre/code/day12/t.txt', 'r') as f:
    print(f.read())

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数

#写文件，换w/wb,追加不覆盖用a
f = open('t.txt', 'a')
f.write(' world!')
f = open('t.txt', 'r')
print(f.read())
f.close()

#等价于：
with open('t.txt', 'a') as f:
    f.write(' world!')

with open('t.txt', 'r') as f:
    print(f.read())

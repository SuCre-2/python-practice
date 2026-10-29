with open('test.txt','w',encoding='utf-8')as f:
    f.write('Hello,world')

with open('test.txt', 'r') as f:
    print(f.read())

#K2
with open('test.txt','a')as f:
    f.write(' How are you')


with open('test.txt', 'r') as f:
    print(f.read())

n = 123
f =456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'hello,"Bart"'
s4 = r'''Hello,
Bob!'''

#print( n,'\n',f,'\n',s1,'\n',s2,'\n',s3,'\n',s4,'\n')
#print(f'100+23={n}\n457.789-1={f}\n{s1}\n{s2}\n{s3}\n{s4}')

s6=int(input('before=:'))
s7=int(input('now=:'))
r=(s7 - s6) / s6 * 100

#print('%.1f%%' %r)
print(f'小明成绩提升了{r:.1f}%')
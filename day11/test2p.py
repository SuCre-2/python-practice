class Student(object):
    pass

class eStudent(object):
    __slots__=('name', 'age')  # 用tuple定义允许绑定的属性名称

class GrStudent(Student):
    def __init__(self, score):
        self.score = score

g  = GrStudent(99)
print(g.score) # 绑定属性'score'，没有报错

s = eStudent()
s.name = 'Michael' 
print(s.name)       # 绑定属性'name'

s.age = 25   
print(s.age)        # 绑定属性'age'

s.score = 99
print(s.score)     # 绑定属性'score'，报错

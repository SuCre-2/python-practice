class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name}在叫')

    def birthday(self):
        self.age += 1
        print(f'{self.name}过生日了，今年{self.age}岁')

d1=Dog('阿旺',4)
d1.bark()

d2=Dog('阿黄',2)
d2.birthday()
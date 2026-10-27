class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def bark(self):
        print(f'{self.name}在叫')

    def birthday(self):
        self.__age += 1
        print(f'{self.name}过生日了，今年{self.__age}岁')

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age < 0:
            raise ValueError('年龄不能为负数')
        self.__age = age


d1=Dog('阿旺',4)
d1.bark()

d2=Dog('阿黄',2)
d2.birthday()
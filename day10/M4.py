class Animal(object):
    def __init__(self,name):
        self.name = name

    def speak(self):
        return '...'

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.__age = age

    def speak(self):
        return '汪汪'

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age < 0:
            raise ValueError('年龄不能为负数')
        self.__age = age

class Cat(Animal):
    def speak(self):
        return '喵'

class GuideDog(Dog):
    pass


animals = [Dog("旺财", 3), Cat("花花"), GuideDog("多多", 5)]
for a in animals:
    print(f"{a.name}:{a.speak()}")
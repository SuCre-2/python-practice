class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("旺财",3)
d.bark()

d2 = Dog("小白",10)
d2.bark()
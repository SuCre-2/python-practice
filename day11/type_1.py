# type()判断对象类型，如果变量指向函数或者类可以判断
# 返回对应的class类型。比如type(123)返回<class 'int'>
# type('str')返回<class 'str'>
# type(None)返回<class 'NoneType'>。
# 如果要判断一个对象是否是函数或者类
# 对class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。
# isinstance()函数可以判断一个对象是否是一个已知的类型
# 或者是否是一个已知类型的子类。
# 如果继承关系是object -> Animal -> Dog -> Husky
# 创建对象a=Animal()，d=Dog(),h=Husky() 
# 那么isinstance(a, Animal)返回True，
# isinstance(d, Dog)返回True，
# isinstance(h, Husky)返回True，
# isinstance(h, Dog)返回True，
# isinstance(h, Animal)返回True，
# isinstance(d, Animal)返回True，
# isinstance()也可以判断type()的返回值，
# 比如isinstance('a', str)返回True，
# isinstance(123, int)返回True，
# 并且可以判断一个变量是否是某些类型中的一种，
# 比如isinstance([1, 2, 3], (list, tuple))返回True，
# isinstance((1, 2, 3), (list, tuple))返回True，
# dir()函数可以获得一个对象的所有属性和方法
# 返回一个包含字符串的list。

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(f'{self.name} 在叫')

    def __dir__(self):
        return ['name','age','bark']

d = Dog('旺财',3)
print(dir(d))

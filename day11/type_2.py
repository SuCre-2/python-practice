class Dog:
    pass

d = Dog()
print(type(d))                       # <class '__main__.Dog'>
print(type(d) == Dog)                # True
print(isinstance(d, Dog))            # True
print(dir(d))                        # 列出所有属性和方法
print(hasattr(d, 'name'))            # False
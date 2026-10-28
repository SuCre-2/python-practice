# class Student(object):
#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.set_score(60) # ok!
# print(s.get_score()) # 60

# s.set_score(9999)  #报错

# def 装饰器(func):          接收被装饰的函数
#     def wrapper(...):      定义新函数（外壳）
#         ...                在这里写你要加的逻辑
#         func(...)          内部再调用原函数
#     return wrapper         返回新函数，把原来的名字顶替掉

# def log_time(func):
#     def wrapper():
#         print("--- 开始 ---")
#         func()
#         print("--- 结束 ---")
#     return wrapper

# def test():
#     print("我是被装饰的函数")

# 关键这一行：手动完成"顶替"
# test = log_time(test)    
# log_time(test) 被调用，参数是原函数 test
# 函数体执行到最后 return wrapper，把内部定义的 wrapper 返回出来
# 然后再把返回的 wrapper 赋值给 test，原来的 test 被替换掉了
# 原来那个函数并没有消失，
# 它被 wrapper 内部的闭包变量 func 记住了。
# 调用 test() 时先进 wrapper，wrapper 再去调原函数。
# test()

# @log_time
# def test():
#     print("我是被装饰的函数")

# #完全等价于：
# def test():
#     print("我是被装饰的函数")
# test = log_time(test)

# 有没有既能检查参数，又可以用类似属性这样简单的方式
# 来访问类的变量呢？
# 装饰器（decorator）可以给函数动态加上功能，
# 对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
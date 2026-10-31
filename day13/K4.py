#序列化，程序运行的时候，内存中的数据都是暂时的，想保留下来就是序列化
#把序列化的结果拿出来可以放到另一个程序/系统运行，可以反序列化重新构建起数据结构和对象
#解决「对象的存储」和「对象的传输」两大问题
#教程例子把字符串序列化成json，利用了dump()函数，
#json.dumps() 默认不知道怎么把一个 Student 实例变成 JSON 的 {} 对象。它只认识 dict、list、str、int、float、bool、None 这些内置类型。
#所以可以用default参数，把类实例转化为字典
#方法1，为类写转化函数
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }

# print(json.dumps(s, default=student2dict))

# 方法2：print(json.dumps(s, default=lambda obj: obj.__dict__))

# 反序列化：
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))

import json

d = {'name': '旺财', 'age': 3, 'tricks': ['sit', 'roll']}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    back = json.load(f)

print(back == d)      # True

# 记事本打开
# {
#   "name": "旺财",
#   "age": 3,
#   "tricks": [
#     "sit",
#     "roll"
#   ]
# }
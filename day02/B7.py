# 知识前览：
# 字典：用key来查值value
# d = {"name":"张三","age":20,"score":95}
# 内含一对对，对应的key与value，之间：分隔，而不同对用，

# 增删改查：
# d["name"]
# 结果是张三，也就是通过key做查找对应的value
# d.get("name")
# 效果如上，多一层若key不存在不报错，而是返回None

# d["age"]=21
# 直接赋值覆盖

# d["city"]=广东
# 新key直接赋值

# del d["score"]
# 删除键，结果是该对被删除
# key是核心
# d.pop("score")
# 删除并且会返回被删的值

# key不可变！
# 可以是字符串数字元组，唯独不能是列表
# 因为list可变

# key必须唯一！

#字典查key，list查位置（0开始）

B7='helloworld'


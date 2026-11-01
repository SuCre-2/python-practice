# a 步：从 sqlalchemy 导入建连接引擎的函数
from sqlalchemy import create_engine
# Column 是「列」类型，Integer 整型列、String 字符串列，都是从 sqlalchemy 导入
from sqlalchemy import Column, Integer, String
# b 步：declarative_base 用来造一个「基类」，表类都要继承它
from sqlalchemy.orm import declarative_base

# b 步：造出基类，取名 Base（注意首字母大写，是个类）
Base = declarative_base()
# a 步：建连接引擎，指向 sqlite 数据库文件 mydatabase.db（三个斜杠是 sqlite 固定写法）
engine = create_engine('sqlite:///mydatabase.db')

# c 步：用类定义表——一个类 = 一张表，类属性 = 表的列
class Student(Base):                  # 继承 Base，SQLAlchemy 靠它认出「这是张表」
    __tablename__ = 'students'        # 表名（双下划线开头的特殊属性）

    id = Column(Integer, primary_key=True)   # 主键列，唯一标识一行，通常自动递增
    name = Column(String)             # 姓名字段，字符串类型
    age = Column(Integer)             # 年龄字段，整型

# d 步：真正在数据库里建表——把上面定义的类翻译成 CREATE TABLE
Base.metadata.create_all(engine)
print('建表完成，mydatabase.db 已生成')

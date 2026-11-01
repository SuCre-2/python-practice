# 导入：建连接、定义列、造基类、开会话、建关联
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# ---- a/b：连接引擎 + 基类 ----
engine = create_engine('sqlite:///mydatabase.db')   # a：连接引擎
Base = declarative_base()                            # b：基类


# ---- c：用类定义表（两张表，一对多）----
class Classes(Base):                                 # 班级表
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # relationship：一个班对应多个学生，SQLAlchemy 会帮你自动查回来
    students = relationship('Student')


class Student(Base):                                 # 学生表
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    # 外键：这一列存的是 classes 表里某行的 id，表示「这个学生属于哪个班」
    class_id = Column(Integer, ForeignKey('classes.id'))


# ---- d：建表 ----
Base.metadata.create_all(engine)


# ---- e/f：会话 + 增删改查 + 一对多 ----
Session = sessionmaker(bind=engine)
session = Session()

# 建一个班
c1 = Classes(name='一班')
session.add(c1)
session.commit()                      # 先 commit，让 c1 拿到 id

# 给这个班加两个学生（class_id 指向 c1 的 id）
session.add_all([
    Student(name='张三', score=85, class_id=c1.id),
    Student(name='李四', score=90, class_id=c1.id),
])
session.commit()

# 查：打印所有学生
print('--- 所有学生 ---')
for stu in session.query(Student).all():
    print(stu.id, stu.name, stu.score, '班级id=', stu.class_id)

# 改：把张三分数改成 99
stu = session.query(Student).filter(Student.name == '张三').first()
stu.score = 99
session.commit()
print('--- 修改后 ---')
for stu in session.query(Student).all():
    print(stu.id, stu.name, stu.score)

# 删：删掉李四
stu2 = session.query(Student).filter(Student.name == '李四').first()
session.delete(stu2)
session.commit()
print('--- 删除后 ---')
for stu in session.query(Student).all():
    print(stu.id, stu.name, stu.score)

# 关键验收点：classes[0].students 能拿到该班的学生列表
classes = session.query(Classes).all()
print('一班的学生：', [s.name for s in classes[0].students])

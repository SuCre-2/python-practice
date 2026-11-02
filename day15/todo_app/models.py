"""数据模型层：只定义「一条待办是什么样子」。

这一层不读写文件、不打印、不处理用户输入。它唯一的职责是：
    1. 造出 Task 对象
    2. 把对象变成能存进 JSON 的字典（to_dict）
    3. 把 JSON 读出来的字典变回对象（task_from_dict）
"""

import datetime


class Task:
    def __init__(self, title):
        # self 指向刚被创建出来的那个对象本身，调用时不用手动传
        self.title = title
        # done 用布尔值而不是字符串"未完成"：
        # 字符串在 if 判断里恒为真值，逻辑会直接出错
        self.done = False
        # 转成 '2026-11-02' 这样的字符串，因为 JSON 没有日期类型，存不了 date 对象
        # 代价：字符串不能直接做日期运算，需要时得用 date.fromisoformat() 转回来
        self.created = datetime.date.today().isoformat()

    def to_dict(self):
        # 把对象拍平成字典。json 模块只认 dict/list/str/int/float/bool/None，
        # 不认 Task，直接 json.dump(对象) 会抛 TypeError: not JSON serializable。
        # 所以序列化必须走两跳：对象 -> 字典 -> 文本。这是第一跳。
        return {
            'title': self.title,
            'done': self.done,
            'created': self.created
        }

    def mark_done(self):
        #改 状态的唯一入口。以后要加完成时间戳、写日志，只改这里一处。
        # 想同时支持「撤销完成」，写成 self.done = not self.done 即可。
        self.done = True


def task_from_dict(d):
    #反序列化的第二跳：字典 -> 对象。

    #为什么不是 Task(**d)：d 的键是 title/done/created，
    #而 __init__ 只接受 title，**d 会抛 unexpected keyword argument 'done'。
    #所以采用「先构造、再补属性」的两段式重建。
    task = Task(d['title'])          # 先造对象，此时 done=False、created=今天
    task.done = d['done']            # 再用文件里的真实值覆盖掉默认值
    task.created = d['created']
    return task


# 只有直接运行本文件时才执行；被 import 时不执行，方便单独测这一层
if __name__ == '__main__':
    t = Task('背八股')
    d = t.to_dict()
    t2 = task_from_dict(d)
    # 打印出来的值和上面三行应该一致，说明往返没丢数据
    print(t2.title, t2.done, t2.created)

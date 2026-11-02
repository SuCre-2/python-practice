"""命令层：菜单 + 四个功能。

每个功能的套路都是三段式：
    records = load()  ->  改 records  ->  save(records)
例外是「列出」，它只读不写。

records 是 list[Task]。存储层已经替我们做好了字典和对象的互相转换，
所以这里取字段一律用 t.title / t.done，全程看不到 JSON 的痕迹。
"""

from models import Task
from storage import load, save


def show(records=None):
    """打印带序号的列表。别的功能都调它，避免三个地方各写一遍循环。"""
    if records is None:
        records = load()
    if not records:
        print('暂无待办')
        return
    # start=1 让用户看到的第一条是 1；列表本身的第一个元素下标仍然是 0
    for i, t in enumerate(records, start=1):
        mark = '[x]' if t.done else '[ ]'
        print(f'{i}. {mark} {t.title}    {t.created}')


def pick(records):
    """让用户挑一条，返回它在列表里的真实下标；出任何问题都返回 None。

    返回下标而不是对象，因为删除要用 pop，切换完成要按下标回写。
    """
    if not records:
        print('暂无待办')
        return None

    show(records)
    raw = input('输入序号：').strip()

    try:
        n = int(raw)
    except ValueError:
        # int('abc')、int('')、int('3.5') 全都走这里
        print('请输入一个整数')
        return None

    # 少了这一句，用户输 99 时 records[98] 会抛 IndexError，程序直接退出
    if not 1 <= n <= len(records):
        print(f'序号要在 1 到 {len(records)} 之间')
        return None

    return n - 1


def add():
    title = input('标题：').strip()
    if not title:
        print('标题不能为空')
        return
    # load() 必须在 append 之前：先读出现有记录，再追加，最后整体写回。
    # 顺序写反就会用「只有新数据」的列表覆盖掉整个文件
    records = load()
    # 这里传的是 Task 对象，不能写成 Task(title).to_dict()。
    # 转字典是 storage.save 内部的事；这里先转成字典的话，
    # save 会对字典调 .to_dict() 而抛 AttributeError
    records.append(Task(title))
    save(records)
    print('已添加')


def list_all():
    # 不能命名为 list —— 会覆盖内置的 list 类型，后面 list() 就没法用了
    show()


def toggle():
    records = load()
    idx = pick(records)
    # 必须用 is None 判断。写成 if not idx 的话，选第 1 条时下标是 0，
    # 0 是假值，程序会误以为「没选」而直接返回
    if idx is None:
        return
    t = records[idx]
    t.done = not t.done
    save(records)
    state = '完成' if t.done else '未完成'
    print(f'已标记为{state}')


def remove():
    records = load()
    idx = pick(records)
    if idx is None:
        return
    t = records.pop(idx)   # pop 会把被删的那条返回，方便回显给用户
    save(records)
    print(f'已删除：{t.title}')


def main():
    while True:
        print('\n1 添加   2 列出   3 切换完成   4 删除   0 退出')
        choice = input('选择：').strip()

        if choice == '1':
            add()
        elif choice == '2':
            list_all()
        elif choice == '3':
            toggle()
        elif choice == '4':
            remove()
        elif choice == '0':
            print('再见')
            break      # while True 是死循环，唯一的出口就是这里的 break
        else:
            print('没有这个选项')


# 只有直接运行 main.py 才进菜单；被 import 时不执行
if __name__ == '__main__':
    main()

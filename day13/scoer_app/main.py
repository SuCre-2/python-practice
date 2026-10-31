#

from storage import load,save

class Score:
    def __init__(self,name,value):
        if not 0 <= value<=100:
            raise ValueError
        self.name = name
        self.value = value

    def grade(self):
        if self.value >= 90:
            return 'A'
        elif self.value >= 80:
            return 'B'
        elif self.value >= 70:
            return 'C'
        elif self.value >= 60:
            return 'D'
        else:
            return 'E'

def add():
    name = input('姓名：')

    while True:
        s=input('分数：')

        try:
            value = int(s)
        except ValueError:
            print('不是数字，请重新输入')
            continue

        try:
            score = Score( name ,value)
        except ValueError as e:
            print(e)
            continue
        break

    records = load()

    records.append({'name':score.name,'value':score.value})

    save(records)

    print(f'已保存：{score.name}{score.value}{score.grade()}')

def show():
    records = load()

    if not records:
        print('暂无记录' )
        return

    print(f'{"姓名":<8}{"分数":<6}{"等级"}')

    for r in records:
        grade = Score(r['name'],r['value']).grade()
        print(f'{r["name"]:<8}{r["value"]:<6}{grade}')


def main():

    while True:               # 主循环：每次处理完一个菜单动作就回到这里
        print('\n1 加  2 查看  3 退出')

        # choice 拿到的是字符串，所以下面和 '1' 比（不是数字 1）
        choice = input('请选择：')

        # try 套住整个「分支判断」部分：
        # 位置很关键 —— 它在 while 内部、分支外部。
        # 放 while 外面：一次异常就退出程序，菜单没了
        # 放进每个分支里面：三个 if 要写三份 except，重复
        try:
            if choice == '1':
                add()                 # 这里可能抛异常，会被下面的 except 接住
            elif choice == '2':
                show()
            elif choice == '3':
                print('再见')
                break                 # break 跳出 while（不是跳出 try），程序结束
            else:
                print('无效选择，请重新输入')

        # 兜底：任何没预料到的异常都在这里被接住，程序继续跑而不是崩掉。
        # as e 保留异常对象，type(e).__name__ 打印异常的类型名（如 KeyError），
        # 后面打印 e 是异常消息。开发阶段一定要看得到这两样，否则你会只看到
        # 一句「出错了」，不知道哪错了。
        except Exception as e:
            print('出错了：', type(e).__name__, e)


# 这行是「只有直接运行本文件才执行 main()」的标准写法。
# __name__ 是 Python 自动给的变量：
#   直接 python main.py 运行时，它是 '__main__'
#   被别的文件 import 时，它是模块名 'main'
# 所以被 import 不会自动弹菜单。
if __name__ == '__main__':
    main()
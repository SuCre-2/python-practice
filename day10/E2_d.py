# E2_d.py —— 完整程序：类 + 取输入 + main
# 单独跑：python E2_d.py


class Score:
    def __init__(self, value):
        # 创建实例时自动调用，self 就是刚建好的这个对象
        # 校验放这里：不合法的分数根本造不出来，后面方法都不用再检查
        if not 0 <= value <= 100:
            raise ValueError('分数必须在 0-100')
        self.value = value

    def grade(self):
        # match + 卫语句：从上往下第一个成立的分支生效
        # 顺序不能乱：先判 >=90 再判 >=80，否则 95 也会落进 80 那支
        match self.value:
            case v if v >= 90:
                return 'A'
            case v if v >= 80:
                return 'B'
            case v if v >= 70:
                return 'C'
            case v if v >= 60:
                return 'D'
            case _:
                return 'E'

    def grade_if(self):
        # 与 grade() 等价的 if/elif 版本，留着对照两种写法
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

    def is_pass(self):
        # 方法名要说清返回什么：这里返回 bool，所以叫 is_pass 名副其实
        return self.value >= 60


def get_score():
    # 输入 + 校验：这是"从外面拿数据"的活，不属于 Score 的职责
    while True:
        s = input('请输入 0-100 的分数: ')
        if not s.isdigit():          # isdigit() 只认真数字符串，"abc"/"-5"/"3.5" 都拦
            print('输入不合法，请重新输入！')
            continue
        n = int(s)
        if 0 <= n <= 100:            # 链式比较，等价于 n >= 0 and n <= 100
            return n
        print('超出范围，请重新输入')


def main():
    score = Score(get_score())
    print('if/elif 评级:', score.grade_if())
    print('match 评级:  ', score.grade())
    print('是否及格:', score.is_pass())


if __name__ == '__&#8203;main__':
    # 只有直接运行本文件才执行；被 import 时不会弹输入框
    main()

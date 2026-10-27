# E2_d_demo.py —— 只看输出，不碰 input
from E2_d import Score


def show(values, title):
    print(f'--- {title} ---')
    for v in values:
        s = Score(v)
        print(f'{v:>3} → grade={s.grade()}  grade_if={s.grade_if()}  is_pass={s.is_pass()}')


# 1. 正常值 + 边界值（59/60、89/90 最容易写错）
show([100, 95, 90, 89, 85, 80, 79, 72, 70, 69, 60, 59, 1, 0], '正常与边界')

# 2. 非法值：构造时就被拦下
print('--- 非法值 ---')
for v in (-1, 101, 200):
    try:
        Score(v)
    except ValueError as e:
        print(f'{v:>3} → 拦住：{e}')

# 3. 两版评级是否完全一致（0-100 逐个比，比手测快得多）
print('--- 两版一致性 ---')
bad = [v for v in range(0, 101) if Score(v).grade() != Score(v).grade_if()]
print('不一致的分数：', bad or '无，0-100 全部一致')

# 4. 实例之间互不影响
print('--- 实例独立 ---')
a, b = Score(85), Score(59)
a.value = 70
print(f'a={a.value} → {a.grade()} ; b={b.value} → {b.grade()}')
print('vars(a) =', vars(a))


#和E2_d一起，主要是重新构造函数成类，让ai改动还有一些新的东西没学会
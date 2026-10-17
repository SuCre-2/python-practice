#match的匹配列表*难点
#假设用户输入一个命令，我们用list存储

args = ['gcc','hello.c','world.c']

#利用match匹配来解析这个列表
#以下是教程示例

match args:
    case ['gcc']:    #只出现gcc报错
        print('gcc:missing source file(s)')
    case ['gcc',file1,*files]:    #出现gcc,而且指定了一个文件
#这一步到底在做什么？
        print('gcc compile : ' + file1 + ',' + ',' .join(files))
    case ['clean']:    #仅出现clean
# 疑问点，join()是做什么的，莫名其妙的变量file1和*和file在做什么？
# clean是为什么，清除？这段代码解释是：
# 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，
# 第二个字符串绑定到变量file1，
# 后面的任意个字符串绑定到*files
# （符号*的作用将在函数的参数中讲解），
# 它实际上表示至少指定一个文件；
# 第三个case ['clean']表示列表仅有'clean'一个字符串
        print('clean')
    case _:
        print('invalid command')

#无法理解，试运行看输出结果

#首先理解.join(),很简单，把括号内的元素用东西连起来

print('yes'.join(['oh','sir']))

#回到匹配列表用法，如下解释

args = ['buy', '拿铁', '可乐', '果茶']

match args:

#情况1：只输入buy，没输入饮品，就提示用户输入饮品

    case['buy']:
        print('请告诉我喝什么饮品!')

#情况2：输入buy和饮品，就告诉用户点了什么饮品

    case['buy', drink1, *other_drinks]:
        all_drinks = drink1 + ',' + ','.join(other_drinks)
        print(f'您点了：{all_drinks}')

#情况3：输入clean，就清理界面

    case['clean']:
        print('正在清理界面')

#情况4：输入其他指令，提示无法识别

    case _:
        print('无法识别的指令，请重新输入！')


#读一个 txt 文件，统计词频，把前 10 名按 单词,次数 的格式写进一个新文件
#思路：读文件->分词->排序->写新文件

def count_words(input_file, output_file, top_n=10):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
#定义函数接受三个参数：1要读取的文件路径，2结果写入的新文件路径，3默认参数，表示取频次最高的前十个词
#with打开文件，代码结束自动关闭
    freq = {}
#定义空子典，记录词->出现频次
    word = ''
#临时变量，累计当前拼装的单词
    for ch in text + '\n':       #遍历 text 的每个字符 ch，并在末尾补一个 '\n'
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            word += ch           #判断是否是字母
        else:
            if word:
                word = word.lower()
                freq[word] = freq.get(word, 0) + 1
                word = ''
#遇到非字母说明单词结束了，.lower大写转小写，这样防止大小写误判两个单词，然后统计
#get(word, 0) 表示从字典取 word 的次数，取不到就返回默认值 0；再加 1 后写回
    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
#排序
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in top:
            f.write(f'{word},{count}\n')    
#写入新文件

if __name__ == '__main__':
    count_words('t.txt', 't_out.txt')

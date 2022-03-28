import re

#
#
# 当文件过大时如何处理,使用readlines进行指定长度分批读取，readlines即使指定读长度在单词的中间，但是仍然会把该行读完
# todo：如果一篇文章末尾和下一行的起始位置是这样的，如何处理:把单词分割开了
# ... ... lo
# ve ... ...
#

# 定义全局的list
word_cnt = {}


# 将读入的文本字符串进行单词处理，按照出现的频次进行排序
def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', ' ', text)

    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = text.split(' ')

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1


# 使用with不需要关闭io流
with open('long_article.txt', 'r', encoding='utf-8') as fin:
    while True:
        lines = fin.readlines(1024)
        if not lines:
            break
        for line in lines:
            parse(line)


# 按照词频排序
sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

# 将列表结果写入文件
# 使用with不需要关闭io流
with open('out3.txt', 'w', encoding='utf-8') as fout:
    for k, v in sorted_word_cnt:
        fout.write('{} : {}\n'.format(k, v))

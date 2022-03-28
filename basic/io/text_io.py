import re


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
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt

# 使用with不需要关闭io流
with open('long_article.txt', 'r', encoding='utf-8') as fin:
    text = fin.read()

sorted_words = parse(text)


# 将列表结果写入文件
# 使用with不需要关闭io流
with open('out2.txt', 'w', encoding='utf-8') as fout:
    for k, v in sorted_words:
        fout.write('{} : {}\n'.format(k, v))



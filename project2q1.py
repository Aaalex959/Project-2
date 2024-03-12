import json

classes = ['crude', 'grain', 'money-fx', 'acq', 'earn']
def count_word_frequency(corpus):
    word_freq = {}

    class_freq = {c: 0 for c in classes}  # 统计每个类别的文档频率

    for doc in corpus:
        doc_id = doc[0]  # 获取文档序列号
        doc_class = doc[1]  # 获取文档类别
        doc_text = doc[2]  # 获取文档内容

        class_freq[doc_class] += 1  # 更新类别的文档频率

        # 统计每个单词在每个类别中的出现次数
        for word in doc_text.split():
            if word not in word_freq:
                word_freq[word] = {c: 0 for c in classes}
            word_freq[word][doc_class] += 1

    return class_freq, word_freq


# 读取文档列表（corpus）从 train.jason 文件
with open('train.json', 'r') as file:
    data = json.load(file)
    corpus = data

class_freq, word_freq = count_word_frequency(corpus)

# 将结果写入 word_count.txt 文件
with open('word_count.txt', 'w') as file:
    # 写入类别的文档频率
    file.write(' '.join(str(class_freq[c]) for c in classes))
    file.write('\n')

    # 写入每个单词在每个类别中的频率
    for word, freq in word_freq.items():
        file.write(word + ' ')
        file.write(' '.join(str(freq[c]) for c in classes))
        file.write('\n')

print("Word count saved to word_count.txt")
import json
from collections import defaultdict

classes = ['crude', 'grain', 'money-fx', 'acq', 'earn']

def count_word_frequency(corpus):
    word_freq = defaultdict(lambda: {c: 0 for c in classes})
    class_freq = {c: 0 for c in classes}

    for doc in corpus:
        doc_class = doc[1]
        doc_text = doc[2]

        class_freq[doc_class] += 1

        seen_words = set()
        for word in doc_text.split():
            if word not in seen_words:
                word_freq[word][doc_class] += 1
                seen_words.add(word)

    return class_freq, word_freq

# 读取文档列表（corpus）从 train.json 文件
with open('train.json', 'r') as file:
    corpus = json.load(file)

class_freq, word_freq = count_word_frequency(corpus)

# 获取词频最高的 10,000 个词
top_words = sorted(word_freq.keys(), key=lambda w: sum(word_freq[w].values()), reverse=True)[:10000]

# 计算每个类别中的总词频
class_word_freq = {c: sum(word_freq[word][c] for word in top_words) for c in classes}

# 将结果写入 word_dict.txt 文件
with open('word_dict.txt', 'w') as file:
    file.write(' '.join(classes))
    file.write('\n')

    for word in top_words:
        file.write(word + ' ')
        file.write(' '.join(str(word_freq[word][c]) for c in classes))
        file.write('\n')

    file.write('Total ')
    file.write(' '.join(str(class_word_freq[c]) for c in classes))

print("Word dictionary saved to word_dict.txt")
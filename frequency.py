# -*- coding: utf-8 -*-
#import pandas as pd
#python3
import re
import jieba
import jieba.analyse
from collections import Counter
import sys
import time
import jieba.posseg as pseg
import codecs
import matplotlib.pyplot as plt
from matplotlib.font_manager import _rebuild
_rebuild()

fread=codecs.open('processed_fineorigin.txt',encoding='utf-8')
stopwords = [line.strip() for line in open('stopword.txt', 'r', encoding='utf-8').readlines()]

c=Counter()
for line in fread.readlines():
    word=jieba.cut(line)
    word=[w for w in word if w not in stopwords]
    for w in word:
        if len(w)>1 and w != '\r\n':
            c[w] += 1

size=[]
labels=[]
for (k,v) in c.most_common(20):
    #print(k,v)
    size.append(v)
    labels.append(k)

plt.rcParams['font.sans-serif']=['SimHei']
plt.pie(size, labels=labels,autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('frequency_stpword.png',dpi=350)

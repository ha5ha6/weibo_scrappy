#-*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import codecs
from collections import Counter
import matplotlib.pyplot as plt
import jieba

def extract_keyword(source,keyword):

    fread=codecs.open(source,encoding='utf-8')
    fwrite=codecs.open('extract_'+keyword+'.txt', 'w',encoding='utf-8')

    try:
        cnt=0
        for i,line in enumerate(fread):
            text = line.strip()
            #print(i,len(text),text)
            if(keyword in text):
                pos1=0
                pos2=len(text)

                cnt+=1
                content = text[pos1 : pos2]
                fwrite.write(str(cnt)+' '+content + '\r\n')
    finally:
        fread.close()
        fwrite.close()

def extract_hashtag(source,keyword):
    fread=codecs.open(source,encoding='utf-8')
    fwrite = codecs.open('extract_'+keyword+'.txt', 'w',encoding='utf-8')
    fhashtag=codecs.open('report_'+keyword+'.txt', 'w',encoding='utf-8')

    try:
        cnt=0
        hashtag=[]
        for i,line in enumerate(fread):
            text = line.strip()

            if("#" in text):

                pos1=0
                pos2=len(text)

                idx=[a for a,x in enumerate(text) if x=='#']
                if len(idx)==1:
                    #print('len1',text[idx[0]:])
                    pass
                else:
                    for j in range(len(idx)-1)[::2]:
                        #print('len>2',j,text[idx[j]+1:idx[j+1]],text)
                        hashtag.append(text[idx[j]+1:idx[j+1]])

                cnt+=1
                content = text[pos1 : pos2]
                fwrite.write(str(cnt)+' '+content + '\r\n')

    finally:
        fread.close()
        fwrite.close()

    c = Counter()

    for hash in hashtag:
        c[hash] += 1

    size=[]
    labels=[]
    for (k,v) in c.most_common(20):
        #print(k,v)
        size.append(v)
        labels.append(k)

    try:
        for k,v in sorted(c.items(), key=lambda x: x[1],reverse=True):
            fhashtag.write(k+':'+str(v) + '\r\n')

    finally:
        fhashtag.close()

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.pie(size, labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('frequency_hashtag.png',dpi=350)

def generate_pie_inrange(keyword,filterfile,stop=True,filter=True,report=True):

    fread=codecs.open('extract_'+keyword+'.txt',encoding='utf-8')

    if filter:
        filterword=[line.strip() for line in open(filterfile, 'r', encoding='utf-8').readlines()]

    if stop:
        stopwords = [line.strip() for line in open('stopword.txt', 'r', encoding='utf-8').readlines()]

    c=Counter()
    for line in fread.readlines():
        word=jieba.cut(line)
        word=[w for w in word if w not in stopwords]
        word=[w for w in word if w not in filterword]
        for x in word:
            if len(x)>1 and x != '\r\n':
                c[x] += 1

    size=[]
    labels=[]
    for (k,v) in c.most_common(40):
        #print(k,v)
        size.append(v)
        labels.append(k)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.pie(size, labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('frequency_inrange_'+keyword+'.png',dpi=350)

    plt.clf()

    plt.barh(labels[:40],size[:40])      # 从下往上画
    #for x, y in enumerate(price):
    #    plt.text(y + 0.2, x - 0.1, '%s' % y)
    #plt.show()
    plt.savefig('frequency_inrangebar_'+keyword+'.png',dpi=350)


    if report:
        freport=codecs.open('report_'+keyword+'.txt', 'w',encoding='utf-8')

        try:
            for k,v in sorted(c.items(), key=lambda x: x[1],reverse=True):
                freport.write(k+':'+str(v) + '\r\n')

        finally:
            freport.close()

source_raw='weibocontent.txt'
source_rough='processed_roughorigin.txt'
source_fine='processed_fineorigin.txt'

#extract_keyword(source_raw,'爱可可-爱生活')
#extract_keyword(source_raw,'http')
#extract_keyword(source_raw,'删除')
extract_keyword(source_rough,'显示地图')
generate_pie_inrange('显示地图','filter.txt')
#extract_keyword(source_fine,'梦')
#generate_pie_inrange('梦','filter.txt')

#extract_hashtag(source_rough,'hashtags')

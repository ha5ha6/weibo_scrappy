#-*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import codecs
from collections import Counter
import matplotlib.pyplot as plt

def extract_keyword(source,keyword):

    fread=codecs.open(source,encoding='utf-8')
    fwrite = codecs.open('extract_'+keyword+'.txt', 'w',encoding='utf-8')

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

source_raw='weibocontent.txt'
source_rough='processed_roughorigin.txt'
source_fine='processed_fineorigin.txt'

extract_keyword(source_raw,'爱可可-爱生活')
extract_keyword(source_raw,'http')
#extract_keyword(source_raw,'删除')
extract_keyword(source_rough,'显示地图')
extract_hashtag(source_rough,'hashtags')

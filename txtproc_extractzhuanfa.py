#-*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import codecs
from collections import Counter
import matplotlib.pyplot as plt

fread=codecs.open('weibocontent.txt',encoding='utf-8')
fwrite=codecs.open('processed_zhuanfa.txt', 'w',encoding='utf-8')
freport=codecs.open('report_zhuanfa.txt', 'w',encoding='utf-8')

try:
    cnt=0
    zhuanfaer=[]
    for i,line in enumerate(fread):
        text = line.strip()

        if("转发了" in text):

            #print(cnt,text.index('了'),text.index('微'))
            zhuanfaer.append(text[text.index('了')+2:text.index('微')-2])

            pos1=0
            pos2 = len(text)
            cnt+=1
            content = text[pos1 : pos2]
            fwrite.write(str(cnt)+ ' '+content + '\r\n')

finally:
    fread.close()
    fwrite.close()

#print(zhuanfaer)
c = Counter()
for zf in zhuanfaer:
    c[zf] += 1

#for (k,v) in c.most_common(1000):
#    print(k,v)

try:
    for k,v in sorted(c.items(), key=lambda x: x[1],reverse=True):
        freport.write(k+':'+str(v) + '\r\n')

finally:
    freport.close()

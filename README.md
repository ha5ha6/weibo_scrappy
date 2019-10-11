## weibo_scrappy
based on 
https://github.com/dingmyu/weibo_analysis 
and
https://www.cnblogs.com/dmyu/p/6034634.html

## step 1: download weibo content

run weibotest.py 

download content as weibocontent.txt

required lib: python selenium

notice: chrome version and chrome drive version should match

## step 2: text processing

### 1. extract 转发 

run txtproc_extractzhuanfa.py

generate processed_zhuanfa.txt

```python
fread=codecs.open('weibocontent.txt',encoding='utf-8')
fwrite=codecs.open('processed_zhuanfa.txt', 'w',encoding='utf-8')

try:
    cnt=0
    zhuanfaer=[]
    for i,line in enumerate(fread):
        text = line.strip()
        if("转发了" in text):
            zhuanfaer.append(text[text.index('了')+2:text.index('微')-2])
            pos1=0
            pos2=len(text)
            cnt+=1
            content = text[pos1 : pos2]
            fwrite.write(str(cnt)+ ' '+content + '\r\n')

finally:
    fread.close()
    fwrite.close()
```

generate report_zhuanfa.txt showing sorted zhuanfa source id in frequency

```python
freport=codecs.open('report_zhuanfa.txt', 'w',encoding='utf-8')

c = Counter()
for zf in zhuanfaer:
    c[zf] += 1
try:
    for k,v in sorted(c.items(), key=lambda x: x[1],reverse=True):
        freport.write(k+':'+str(v) + '\r\n')
finally:
    freport.close()
```

generate frequency_zhuanfa.png showing top 20 resourcer in pie chart

```python
size=[]
labels=[]
for (k,v) in c.most_common(20):
    size.append(v)
    labels.append(k)
    
plt.rcParams['font.sans-serif']=['SimHei']
plt.pie(size, labels=labels,autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('frequency_zhuanfa.png',dpi=350)
```


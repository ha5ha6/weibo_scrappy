## weibo_scrappy

## step 1: download weibo content

run weibotest.py 

download content as weibocontent.txt

require lib: python selenium

notice: chrome version and chrome drive version should match

## step 2: text processing

### 1. extract rough origin

run txtproc_roughorigin.py

remove 转发的微博, 赞[0], [组图共？张]

remain [自己可见], hashtag, https, 表情, 显示地图

generate processed_roughorigin.txt

```python
fread=codecs.open('weibocontent.txt',encoding='utf-8')
fwrite = codecs.open('processed_roughorigin.txt', 'w',encoding='utf-8')

try:
    for i,line in enumerate(fread):
        text = line.strip()
        pos1 = 0
        if("转发了" not in text and "原图" not in text and "赞[" not in text and "转发理由" not in text):
            pos2 = len(text)
            if(-1 != text.find("[组图共")):
                pos2 = text.find("[组图共")

            content = text[pos1 : pos2]
            fwrite.write(content + '\r\n')
finally:
    fread.close()
    fwrite.close()
```

### 2. extract fine origin

run txtproc_fineorigin.py

require lib: re

remove everything in [], including [表情/好友圈可见/自己可见/密友可见/地点], 显示地图, 分享图片 using re

```python
fread=codecs.open('processed_roughorigin.txt',encoding='utf-8')
fwrite = codecs.open('processed_fineorigin.txt', 'w',encoding='utf-8')

pattern1 = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pattern2 = re.compile(r'分享图片')
pattern3 = re.compile(r'显示地图')

content=re.sub(u"\\[.*?]","",text) #remove []
content=re.sub(u"\\#.*?#","",text) #remove ##
content=re.sub(pattern1, "",content) #remove http
content=re.sub(pattern2,"",content) #remove '分享图片'
content=re.sub(pattern3,"",content) #remove '显示地图'
```

generate processed_fineorigin.txt

### 3. generate word frequency

run frequency.py

require lib: jieba, stopword.txt, python3 font SimHei setup with matplotlib

```python
fread=codecs.open('processed_fineorigin.txt',encoding='utf-8')
stopwords = [line.strip() for line in open('stopword.txt', 'r', encoding='utf-8').readlines()]

c=Counter()
for line in fread.readlines():
    word=jieba.cut(line)
    word=[w for w in word if w not in stopwords]
    for w in word:
        if len(w)>1 and w != '\r\n':
            c[w] += 1
```

generate frequency.png showing top 20 in piechart

<img src="https://github.com/ha5ha6/weibo_scrappy/blob/master/frequency_stopword.png" alt="drawing" width="600"/>

<!--- ![alt text](https://github.com/ha5ha6/weibo_scrappy/blob/master/frequency_stpword.png) --->

### 4. extract 转发 

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

### 5. extract hashtag, https, content fr specific source id

generate processed_fineorigin.txt

generate report_hashtag.txt, frequency_hashtag.png (piechart)

generate report_http.txt





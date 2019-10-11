#-*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import codecs
from collections import Counter
import matplotlib.pyplot as plt
import re

fread=codecs.open('processed_roughorigin.txt',encoding='utf-8')
fwrite = codecs.open('processed_fineorigin.txt', 'w',encoding='utf-8')

try:
    cnt=0

    for i,line in enumerate(fread):
        text = line.strip()

        pattern1 = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        pattern2 = re.compile(r'分享图片')
        pattern3 = re.compile(r'显示地图')
        
        content=re.sub(u"\\[.*?]","",text) #remove []
        content=re.sub(u"\\#.*?#","",content) #remove hashtag
        content=re.sub(pattern1, "",content) #remove http
        content=re.sub(pattern2,"",content) #remove '分享图片'
        content=re.sub(pattern3,"",content) #remove '显示地图'

        fwrite.write(content + '\r\n')

finally:
    fread.close()
    fwrite.close()

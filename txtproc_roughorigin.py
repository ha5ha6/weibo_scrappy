#-*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import codecs

fread=codecs.open('weibocontent.txt',encoding='utf-8')
fwrite = codecs.open('processed_roughorigin.txt', 'w',encoding='utf-8')

try:
    for i,line in enumerate(fread):
        text = line.strip()
        #print(i,len(text),text)
        pos1 = 0
        if("转发了" not in text and "原图" not in text and "赞[" not in text and "转发理由" not in text):

            pos2 = len(text)
            #if(-1 != text.find("http")):
            #    pos2 = text.find("http")
            if(-1 != text.find("[组图共")):
                pos2 = text.find("[组图共")

            content = text[pos1 : pos2]
            fwrite.write(content + '\r\n')

finally:
    fread.close()
    fwrite.close()

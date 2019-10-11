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

### extract 转发 

run txtproc_extractzhuanfa.py

generate processed_zhuanfa.txt

generate report_zhuanfa.txt showing sorted zhuanfa source id in frequency

generate frequency_zhuanfa.png showing pie chart


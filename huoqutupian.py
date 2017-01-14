# -*- coding: utf-8 -*-
import re
import requests  #导入一个库文件，用于处理图片

#读取源代码
f = open('c.txt','r')
html = f.read()
f.close()

#匹配图片的网址
pic_url = re.findall('href="//(.*?)">',html,re.S)
i = 0
for each in pic_url:
    print 'now downloading:' + each
    pic = requests.get(each)
    fp = open('haha\\' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
print each
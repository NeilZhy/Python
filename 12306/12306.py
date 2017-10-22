
# -*- coding: utf-8 -*-

import urllib2
import ssl
from json import loads

#关闭安全证书
ssl._create_default_https_context = ssl._create_stdlib_context

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def getTrainList():
    req = urllib2.Request("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-20&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT")
    req.headers  = headers
    html = urllib2.urlopen(req).read() #这个是什么Python的数据类型呢,这个是string,实际上就是json数据
    result = loads(html) #将json数据转成字典数据了
    return result['data']['result']

c = 0
for i in getTrainList():
    tmp_list = i.split('|') #通过|进行分隔
   # for n in tmp_list:
    #    print '[%s] %s' %(c,n)
     #   c += 1 #通过观察可以发现，软卧的索引是23，硬卧的索引是28
    if tmp_list[23] == u'有' and tmp_list[23] != u'无' and tmp_list[23] != '':
        print '有票' #这里判断的时候少了一层就是，不满足上面的条件的时候是不是为0，这个为0没有判断
    else:
        print '没票' #不加上上面的判断是不是0的判断也是可以的

#-*-coding:utf8-*-

#导入map所在的Pool这个类，然后重新命名为ThreadPool
#导入requests抓取网页源代码
#导入time计算时间，比较单线程和多线程的时间
from multiprocessing.dummy import Pool as ThreadPool
import requests
import time

#定义了一个函数，其作用是获取传入的URL的源代码
def getsource(url):
    html = requests.get(url)

urls = []

#下面的这些代码生成20行网址，这里range函数使用头但是不使用尾，所以这里传入的是21
for i in range(1,21):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
    urls.append(newpage)  #将这二十个网址全部添加到urls这个列表里面

time1 = time.time()  #该语句的作用是记下程序运行到这一步的时间
for i in urls:
    print i
    getsource(i)
time2 = time.time()  #记下时间2
print u'单线程耗时：' + str(time2-time1)  #两个时间相减就是上面这段代码执行完的总时间

#使用Python的并行化操作
pool = ThreadPool(4)  #初始化一个实例
time3 = time.time()
results = pool.map(getsource, urls)  #使用getsource和map函数进行爬取
#map的作用就是并行的处理getsource这个函数，然后传入的是urls的内容
pool.close()
pool.join()
time4 = time.time()
print u'并行耗时：' + str(time4-time3)

#运行结果是单线程爬虫比多线程爬虫的时间要长的多

#这里map只是做一个了解，以后还会讲到scrypy
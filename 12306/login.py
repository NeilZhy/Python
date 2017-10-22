
# -*- coding: utf-8 -*-

import urllib2,urllib
import ssl
import cookielib
from json import loads

c = cookielib.LWPCookieJar() #存储cookie对象的一个容器，这个可以做到让我们的浏览器是一个为一个浏览器访问的
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)
urllib2.install_opener(opener)


ssl._create_default_https_context = ssl._create_stdlib_context  #验证证书的



heads = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
} #heads就是一个模拟浏览器的内容，这是一个字典的形式

#这里的getcode和login函数，它是两个函数，也可以理解为这里相当于是打开了两个浏览器，所以你登陆的和我获取验证码不是在一个内容之内的，所以我们这里需要考虑一个问题就是，如何让这两个内容放置在一个内容之内的
#所以我们需要通过编程的手段，让我们的浏览器知道我们这两个函数是在一个之内的
def getcode():
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4686358144561331')
    req.headers = heads
    #codeFile = urllib2.urlopen(req).read()
    codeFile = opener.open(req).read()
    with open('code.png','wb') as fn:
        fn.write(codeFile)


def login():
    getcode()
    code = raw_input('请输入验证码：')
    req = urllib2.Request("https://kyfw.12306.cn/passport/captcha/captcha-check")
    #req就是一个请求对象,意思就是说，我们实例化了一个访问上面网址的一个对象
    req.headers = heads  #把这个对象的头设置为上面的
    data = { #这里实际上使用的是一个post方法，post方法即是这个样子的，就是我们的url上面是有参数的，就是我们的浏览器会给服务器发送一些列的参数
        #'answer': '256, 48',
        'answer': code,

        'login_site':'E',
        'rand':'sjrand',
    }
    data = urllib.urlencode(data) #上面的data是一个字典，但是我们的服务器查询的时候是需要用到查询字符串的格式的，所以这里使用了一个函数，把自电脑转化成查询字符串的格式
    #print data
   # html = urllib2.urlopen(req,data=data).read()   #打开一个网站，要么是一个url，要么是一个url的对象
    #使用上面的函数返回了一个返回值，这个返回值是一个request对象，我们是需要拿到这个返回值的
    html = opener.open(req,data=data).read()   #打开一个网站，要么是一个url，要么是一个url的对象

    #print html
    #本次的链接是填写 验证码的方式

    result = loads(html)
    if result['result_code'] == '4':
        print '验证码验证成功'
        req = urllib2.Request('https://kyfw.12306.cn/passport/web/login')
        req.headers = heads
        data = {
            'username': '18729053056',
            'password': 'NEIL1110',
            'appid': 'otn',
        }
        data = urllib.urlencode(data)
        html = opener.open(req,data=data).read()
        print html
    else:
        print '验证码验证失败'
        login()
login()
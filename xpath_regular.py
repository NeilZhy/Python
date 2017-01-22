#-*-coding:utf8-*-
from lxml import etree  #导入etree
#下面是一个多行字符串，实际就是一个小网页的源代码
html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>
'''

selector = etree.HTML(html)  #使用etree将多行字符串转化成XPath可以识别的对象，然后传递给selector

#提取文本
#运行的结果是打印出了“这是第一条信息，这是第二条信息，这是第三条信息”

#运用XPath中的/text()获取标签li里面的内容，其中id="useful"，限定了ul，而不是所有的ul
#这里如果我们把限定条件给去掉，下一句的代码变成了content = selector.xpath('//ul/li/text()')
#则打印的结果是“这是第一条信息，这是第二条信息，这是第三条信息，不需要的信息1，不需要的信息2，不需要的信息3”
#因为这里的ul[@id="useful"]是独一无二的，我们不必担心，当然，如果我们想保险一点的话，还可以在ul的前面，加上他的上一层标签
#//div/ul[@id="useful"]/li/text()我们还可以在div的后面添加代码变成div[@id="content"]
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print each

#提取属性,下面代码的运行结果是打印出上面网页代码中的两个链接
#这里就使用了上文所讲的方式，提取属性内容：/@xxxx      (xxxx是属性的名字)
#这里的网页比较简单，当我们做其他的操作时，肯定不能像这个一样，我们就可以像上文一样给它加限定比如下面的代码
#//div[@id="url"]/a/@href
link = selector.xpath('//a/@href')
for each in link:
    print each

#下面这段代码的结果是提取“极客学院课程库”这些内容，大家可以尝试一下
title = selector.xpath('//a/@title')
print title[0]



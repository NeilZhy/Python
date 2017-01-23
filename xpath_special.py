#-*-coding:utf8-*-
from lxml import etree

#首先将一下下面代码的困难之处，在html1中的body标签下的div标签里面，有三个id，且三个id不同
#这就是我们需要处理的第一类问题，以相同的字符开头的情况
html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''

#在接下来的html2中出现标签套标签
html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''

selector1 = etree.HTML(html1)
#下面代码里面//div[starts-with(@id,"test")]/text()'注意讲到的一个新用法，这里的意思是，标签id中以“test”开头的所有标签都会被提取出来
#运行的结果是“需要的内容1，需要的内容2，需要的内容3”
content1 = selector1.xpath('//div[starts-with(@id,"test")]/text()')
for each in content1:
    print each

#下面的代码是标签套标签的错误使用，就是我们利用上一章节的使用方法
#直接提取div[@id="test3"]，运行的结果是只能提取div里面的内容，而div里面嵌套的标签的内容无法提取
#运行的结果是“我左青龙  龙头在胸口”，这显然不是我们想要的内容
selector2 = etree.HTML(html2)
content_2 = selector2.xpath('//div[@id="test3"]/text()')
for each in content_2:
    print each

#下面的内容就是我们提取的完整的内容
#我们这里的思想还是先大后小的思想，我们先提取div下面的所有的内容
#然后直接使用info = data.xpath('string(.)')，但是注意的是这一句执行的结果会把换行，空格都给提取出来
#所以我们需要使用替换，把换行符合空格符全部替换掉
#运行的结果是我左青龙，右白虎，上朱雀，下玄武。老牛在当中，龙头在胸口。
selector3 = etree.HTML(html2)
data = selector3.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
content_3 = info.replace('\n','').replace(' ','')
print content_3
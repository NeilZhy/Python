#coding=utf-8
#统计所有单词的词频
fn = 'a.txt'

fr = open(fn,'r')
cont = fr.read()
cont = cont.replace('.',' ')   #替换标点符号
cont = cont.replace(',',' ')
cont = cont.replace('!',' ')
cont = cont.replace(':',' ')
cont = cont.replace('(',' ')
cont = cont.replace(')',' ')
cont = cont.replace('-',' ')
cont = cont.replace('/',' ')

li = cont.split()    #将cont分割，以空格分开，括号里面填写的是分割的标志,生成一个列表li

t = list()   #新建一个列表
for x in li: #遍历把无重复单词放置在列表t中
    if x not in t:
        t.append(x)

for x in t:     #在t总遍历，然后每次统计一次词频
    f = 'b.txt'
    fw = open(f, 'a')   #a的属性是在原有的基础上面写
    fw.write(x)
    fw.write("的词频为")
    fw.write(str(li.count(x) * 1.0 / len(li)))
    fw.write("\n")

fw.close()
fr.close()
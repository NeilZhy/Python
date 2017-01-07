#coding=utf-8
#统计某个单词的词频
fn = 'a.txt'
fr = open(fn,'r')
cont = fr.read()
cont = cont.replace(',',' ')  #替换前一个字符为后一个字符，这里要统计单词的个数，所以要把标点符号替换掉
cont = cont.replace('.',' ')
li = cont.split()  #分割单词
for x in li:
    print x
s = "the"
c = 0
for x in li:
    if x == s:
        c += 1
print c
print c * 0.1 / len(li)
print li.count("Xuzhou") * 0.1 / len(li)      #统计列表中某个字符的个数
print set(li)      #得到一个列表中的所有单词，如果有重复的就统计一次，且按照顺序显示
fr.close()

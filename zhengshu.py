fn = 'output.txt'
fw = open(fn,'w')
i = 0
while i < 10000:
    i += 1
    fw.write(str(i) + '\n')
    print i,
fw.close()
'''
jiang 1-1000 xie ru dao wen jian zhong qu
'''
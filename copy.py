#copy
f1 = 'a.txt'
f2 = 'b.txt'
fr = open(f1,'r')
cont = fr.read()#duqu ranhou fanhui gei cont
fr.close()
fw = open(f2,'w')
fw.write(cont)
fw.close()
#copy
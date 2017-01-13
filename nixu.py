fr = open('copy.py','r')
li = fr.readlines()
fr.close()
li = li[::-1]   #nixu xieru
fw = open('temp.py','w')
fw.writelines(li)
fw.close()
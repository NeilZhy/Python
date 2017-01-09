#coding=utf-8
import os
import time
f = open('c.txt','r')
content = f.read()
os.system(content)
time.sleep(5)
f.close()
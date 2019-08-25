# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:00:50 2017

@author: Administrator
"""

help (open)
f = open('test.txt')
print (f)
print (f.read())
print ('已經被讀書了,沒有內容可讀了')
print (f.read())
f.close()

f = open('test.txt')
print ('只讀前面 10 個字 (包括中英文)')
print (f.read(10))
print ('顯示目前指標位置 (顯示 12 是因為中文字代表二個 byte)')
print (f.tell())
f.close()

f = open('test.txt')
f.seek(41,0)
print (f.readline())
f.close()

print ('\n將檔案內轉成 list 再取出各行的效率很低')
f = open('test.txt')
print (list(f))
f.close()

print ('\n要 list 各行,官方文件如下')
f = open('test.txt')
for each_line in f:
    print (each_line)
f.close()


print ('\n文件寫入')
f = open('test_write.txt', 'w')
f.write('I love python.')
lst = ['first \nsenond\nthrid']
f.writelines(lst)
f.write('aaa')
f.close()

f = open('test_write.txt')
print (f.read())



print ('\n\nos')
import os
print ('目前工作路徑')
print (os.getcwd())
#print ('目前工作路徑')
#print (os.chdir('C:\\'))
print (os.getcwd())
#os.system('cmd')
#os.system('calc')

print ('os.path')
print ('join 時硬碟有帽號的部分要加斜線, 其中不用')
dir = os.path.join('C:', '$MyDoc','Project')
print (dir)
print (os.path.isdir(dir))
dir = os.path.join('C:\\', '$MyDoc\\','\\Project')
print (dir)
print (os.path.isdir(dir))
dir = os.path.join('C:\\', '$MyDoc','Project')
print (dir)
print (os.path.isdir(dir))

import time
print ('\ntime info')
print (time.localtime(os.path.getctime('test.txt')))
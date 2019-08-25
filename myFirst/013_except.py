# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:52:05 2017

@author: Administrator
"""

print ('\nexcept 1')
try:
    f = open('我是一個不存在的檔案.txt')
    print (f.read())
except OSError:
    print ('文件存取出錯了')
    
print ('\nexcept 2 : 取得詳細內容')
try:
    f = open('我是一個不存在的檔案.txt')
    print (f.read())
except OSError as reason:
    print ('文件存取出錯了. 原因 : ' + str(reason))    

   
print ('\nexcept 3 : 多項 except 判斷')
try:
    sum = 3 + '33'
    f = open('我是一個不存在的檔案.txt')
    print (f.read())
except OSError as reason:
    print ('文件存取出錯了. 原因 : ' + str(reason))
except TypeError as reason:
    print ('型別操件錯誤. 原因 : ' + str(reason))

    
print ('\nexcept 4 - finally')
try:
    f = open('我是一個不存在的檔案.txt','w')
    print (f.write('我存在了'))
    sum = 22 + '33'
except OSError as reason:
    print ('文件存取出錯了. 原因 : ' + str(reason))
except TypeError as reason:
    print ('型別操件錯誤. 原因 : ' + str(reason))
finally:
    print ('檔案要關閉')
    f.close()


    
print ('\nexcept 5 - raise')
try:
    #raise ('沒錯也要報錯.')
    raise (ZeroDivisionError('除數不得為 0 '))
    print (f.write('我存在了'))
    sum = 22 + '33'
except OSError as reason:
    print ('文件存取出錯了. 原因 : ' + str(reason))
except TypeError as reason:
    print ('型別操件錯誤. 原因 : ' + str(reason))
except ZeroDivisionError as reason:
    print ('未指定特定錯誤. 原因 : ' + str(reason))

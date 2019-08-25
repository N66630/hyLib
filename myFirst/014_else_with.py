# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:13:35 2017

@author: Administrator
"""

print ('\nwhile else')
def ShowMaxFactor(num):
    count = num // 2
    while (count > 1):
        if num % count == 0:
            print ('%d的最大量為 : %d' % (num, count))
            break;
        count-=1
    else:
        print ('%d是一個質數' % (num))
ShowMaxFactor(16)
ShowMaxFactor(17)


print ('\ntry except else')
try:
    print (int('abc'))
except ValueError as reason:
    print ('出錯了 : ' + str(reason) )
else:
    print ('沒有異常')



print ('\nwith')
#try:
#    f = open ('abcdef.txt')
#    for each_line in f:
#        print (each_line)
#except OSError as reason:
#    print ('出錯了 : ' + str(reason) )
#finally:
#    f.close()

print ('上面因為檔案不存在,所以 f 變數是 none, 在 finally 中要執行 f.close() 會錯')
try:
    with open ('abcdef.txt') as f:
        for each_line in f:
            print (each_line)
except OSError as reason:
    print ('出錯了 : ' + str(reason) )
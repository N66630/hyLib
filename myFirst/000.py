# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:25:49 2017
@author: Administrator
"""

# 1. 註解可以是 # 或 """ (內容可以用跳脫字元)
## 2. print 
## 底下這行是 2 版本的寫法, 在版本 3 會錯 
# print "Hello World"
## 2.1 另一種註解
"""
print ("Hello World !!")
print ("Hello World !!", 1234, 0.000000000023, "Test1")
print (123456789*123456789)
print ("I love " + "you")
print ("I love you\n" * 3)
"""
print ("""hello,
I am are student.""")

## 3. BIF : Built in Function 命令 (python command)
#print (dir(__builtins__))
## help
#print (help (input))
#print (help (int))

 
## 4. 變數 : 需先給值
#print ('變數需先給值')
#sTest = "Let\'s Go"
#print (sTest)
#print ('字串中的跳脫字元')
#sTest = "C:\\\\tmpe\\"
#print (sTest)
## r"" 最後不能加反斜線
#print ('最後不能加反斜線,只能會串聯的方式才不會錯')
#sTest = r"C:\\temp" + "\\"
#print (sTest)
#sTest = """
#這是一個
#可以有跳脫字元
#的字串
#"""
#print (sTest)

 
## 4. number
#print (0.000000000000000000000034)
#print (3.4e-10)
## 取無符號的最小整數後再加上符號 (無條件去除小數部分後加上正負符號)
## 5
#print (int(5.99))
## -5
#print (int(-5.99))
## 5.0
#print (float(5))
#print (float (1e+2))
#print (str (1e+2))

 
## 5. boolean
## 1 (True is 1, False is 0)
#print (True)
## 2 (True is 1, False is 0)
#print (True + True)

## 9. type, isinstance
#print (type(23.0))
#print (isinstance(2342, int))
#print (isinstance(2.34, float))
#print (isinstance(2342, int))
#print (isinstance(True, bool))

 
## 10. 運算符號 : 幂運算 (**) > 正負號 > 算術操件符號 (* / // + -)
##              > 比較操作符 (< <= > >= == !=) > 邏輯操作符 (not and or)
## 取小的整數結果
#print (10 // 8)
#print (3.0 // 2)
## 取餘數
#print (10 % 8)
#print (3.0 % 2)
## 次方
#print (3**3)
#print (3**5)
## ** > 負號
#print (-3**2)

#print (3 < 4 < 5 < 6)

 
## 11 三元操件符
#a = "Y"
#b = "N"
#x = 4
#y = 5
#result = a if x < y else b
#print (result)

 
## 12 assert (拋出 AssertionError)
#assert 3<4
#assert 3>4
 
 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:15:16 2017
@author: Administrator
"""

# 三個雙引號的注解可以包含跳脫字元
#str = """
#Hello, world
#    This is my first python ap
#good bye!!
#"""
#print (str)

# 查詢 python 的合部內建函數與 help
#pythonfunc = (dir(__builtins__))
#for func in pythonfunc:
#    print (func, len(func))
#help(int)

# 單行判斷式 (IIF)
#x, y = 4, 5
##if x < y:
##    small = x
##else:
##    small = y
#small = x if x < y else y
#print (small)

# assert 判斷式 (如果判斷式中不合法會 exception)
#assert 5 < 4

# 九九乖法
#print ('-------我的第一個 python 應用程式-------')
#num = input ('請輸入乘法表的最大數目 : ')
#inputtype = type(num)
#if isinstance(num, int):
##if inputtype == 'int':
#    for x in range(1, num+1, 1):
#        for y in range(1,num+1, 1):
#            print (str(x) + ' * ' + str(y) + ' = ' + str(x*y))
#else:
#    print('It\'s not a integer')

# 陣列
myarr = ['ab','cd','dde']
print ('陣列長度 len(myarr) : ' + str(len(myarr)))
myarr.append('AppendStr')
print ('append 一個陣列元素後的陣列長度 : ' + str(len(myarr)))
myarr.extend(['ext1','ext2'])
print ('extend 一個陣列元素後的陣列長度 : ' + str(len(myarr)))
myarr.insert(3, 'InsertData')
print ('在第 3 個位置插入一個值後的陣列內容 : ')
print (myarr)
myarr.remove('cd')
print ('移除 cd (remove) 的項目之後的陣列內容 : ')
print (myarr)
del myarr[1]
print ('移除索引 1 之後的陣列內容 : ')
print (myarr)
print ('列印索引 1-3 的陣列內容 : ')
print (myarr[1:3])
myarr2 = myarr
myarr[0] = 'aaaaa'
print ('將陣列指定給 myarr2 後再將 myarr[0] 指定為 aaaaaa 後列出陣列內容 (二個) : ')
print (myarr)
print (myarr2)
myarr2 = myarr[:]
myarr[0] = 'ABAB'
print ('將陣列指定給 myarr2 ([:]), 後再將 myarr[0] 指定為 ABAB 後列出陣列內容 (二個) : ')
print (myarr)
print (myarr2)
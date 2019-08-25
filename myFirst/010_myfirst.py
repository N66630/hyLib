# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:17:18 2017

@author: Administrator
"""

## 1. while
#import random
#
#print ('------------------------- start ------------------------')
#secret = random.randint(1, 10)
#temp = input("猜數字,請輸入一個數字 : ")
#guess = int (temp)
#while guess != secret:
#    if guess > secret:
#        print ("哈哈!沒猜中 - 太大了")
#    else:
#        print ("哈哈!沒猜中 - 太小了")
#    temp = input("請再猜一次 : ")
#    guess = int (temp)
#
#if guess == secret:
#    print ("恭喜您猜中了, 一路發了")
#print ("結束了")

 
## 2. if else
#print ('------------------------- 輸入成績 ------------------------')
#temp = int(input ('請輸入成績 : '))
#while not isinstance (temp, int):
#    temp = input ('輸入的值非數值, 請重新輸入 : ')
#n = int(temp)
#if (100 >= n > 80):
#    print ("A")
#elif (80 > n >= 60):
#    print ("B")
#elif (60 > n >= 0):
#    print ("C")
#else:
#    print ("E")

 
 
## 3. for / range
## 3.1 
#for c in "abcd":
#    print (c)
#for c in "abcd":
#    print (c,',')
#for c in "abcd":
#    print (c,end=',')
#    
## 3.2
#ar = ['AA','BBB','C','中文','EE']
#for s in ar:
#    print (s + ' : ' + str(len(s)))
#    print (s, len(s))
#
## 3.3
## 宣告深度為 5 的陣列
#ar = range (5)
## 印出陣列
#print (ar)
## 列出陣列 0~4
#print (list (range(5)))

## 3.4 
#for i in range (5):
#    print(i)
#for i in range (10, 100, 10):
#    print(i)

 
 
 
## 4 break / continue
#gv = "roylai"
#guess = input ("猜猜我的名字 : ")
#while True:
#    if (guess == gv):
#        print ("勵害, 猜對了")
#        break;
#    guess = input ("抱歉, 猜錯了, 請重新猜或輸入q離開 : ")
#    if (guess != "q"):
#        continue;
#    else:
#        break
#print ("結束了")

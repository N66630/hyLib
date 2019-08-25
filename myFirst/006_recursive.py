# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:32:47 2017

@author: Administrator
"""

print ('\nrecusion')
print ('設定最大階層, 預設 100 層')
import sys
sys.setrecursionlimit(1000000)
 
print ('\n非遞歸函數寫法')
def factorial(n):
    r = n
    for i in range(1, n):
        r *= i
    return r
num = 5
result = factorial(num)
print ('%d 的階層是 %d' % (num, result))
 
print ('遞歸函數寫法')
def recusive(n):
    if n == 1:
        return 1
    else:
        return n * recusive(n-1)
num = 10
result = recusive(num)
print ('%d 的階層是 %d' % (num, result))
 
 
print ('\nfibonacci 數列 (1,1,2,3,,5,8,13,21,34,55)')
print ('\n注意 : 遞歸需要耗很多資源, 當底下二個 function 的 n 代入越多時, iterable & recursive 會差越多')
def fib(n):
    n1=1
    n2=1
    n3=1
    if n < 1:
        print ('不合法輸入')
        return -1
    while (n-2) > 0:
        n3=n2+n1
        n1=n2
        n2=n3
        n -= 1
    return n3
print (fib(8))
 
def fib(n):
    if n < 1:
        print ('不合法輸入')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print (fib(9))


print ('\n河內塔 (hanoi, 漢諾塔)')
print ('演算法 : (起始柱, 暫存柱, 目標柱)')
print ('1. 將 (n-1) 的盤子由啟始柱移到暫存柱')
print ('2. 將 (n) 的盤子由啟始柱移到目標柱')
print ('3. 將 (n-1) 的盤子由暫存柱移到目標柱')
def hanoi(n, source, target, temp):
    if (n > 0):
        hanoi(n-1, source, temp, target)    # 將 (n-1) 的盤子由啟始柱移到暫存柱
        print ('%s --> %s\t[%d]' % (source.ljust(6), target.ljust(6), n))  # 將 (n) 的盤子由啟始柱移到目標柱
        hanoi (n-1, temp, target, source)   # 將 (n-1) 的盤子由暫存柱移到目標柱
hanoi(3,'Source','Target','Temp')


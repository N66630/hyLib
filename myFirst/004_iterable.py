# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:02:40 2017

@author: Administrator
"""

## 序列都是一種迭代 (iterable)
# help (list)
# help (tuple)

# 內建函數


a = list()
print (a)

b = "I Love You"
print (list(b))

print ('\ntuple 把一個可迭代的對象轉換為元組'   )
c = (1,1,2,3,5,8,13,21,34)
print (list(c))

print ('\nstr(obj) 把引數中的對象轉換為字串'   )
print (str(c))

print ('\nmax(iterable) : 要是同類型'   )
print (max(1,2,3,4,5))
print ('max(iterable) : 字串由第一字元開始比'   )
print (max('a','b','c','d','e','eaa'))


print ('max(iterable) / min()'   )
print (min('abcdef'))
tuple1 = (1,2,3,4,5,6,7,8,9)
print (max(tuple1))

print ('\nsum(iterable,[start=0]) : iterable sum 完後再加 start 中的值')
print (sum(tuple1, 3))

print ('\nsorted(iterable) : 同 list.sort()')
tuple1 = (4,3,6,7,2,8)
print (sorted(tuple1))

print ('\nreversed(iterable) : 同 list.reverse()')
print (list(reversed(tuple1)))

print ('\nenumerate(iterable) : 每個元素加上一個 index 變為 tuple 元素')
print (list(enumerate(tuple1)))

print ('\nzip(iterable) : 每個元素合併二個 iterable 變為 tuple 元素, 長度為二個 iterable 中最小的長度')
tuple2 = (2,4,6,8)
print (list(zip(tuple1, tuple2)))

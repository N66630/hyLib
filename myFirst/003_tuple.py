# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:47:31 2017

@author: Administrator
"""

print ("\rtuple 要 list 差不多, 但 tuple 不可以變更元素內容, list 可以 (最大不同)")
print ("\rtuple 以小刮號刮住數值, 也是以逗號分隔")
tuple_1 = ("A","B",12, ["AA","BB"],12.34)
print (tuple_1)
print ("\rprint index [3] of tuple (\"A\",\"B\",12,[\"AA\",\"BB\"]) of index is 3: ")
print (tuple_1[3]);
print ("\rprint index [3][0] of tuple ([\"A\",\"B\",12,[\"AA\",\"BB\"]]) : ")
print (tuple_1[3][0], len (tuple_1[3][0]), 123, 0.00000000023, "Test1", "Test2");
 
print ("\r因為 tuple 內的裡不能變更, 所以沒有 append, remove, insert, pop 等方法 : ")
print (dir(tuple))
 
print ("\rtuple 複製: ")
print (tuple_1)
tuple_new = tuple_1[:]
print (tuple_new)
tuple_new = tuple_1[1:]
print (tuple_new)
tuple_new = tuple_1[:3]
print (tuple_new)
tuple_new = tuple_1[0:2]
print (tuple_new)
 
print ("\rtuple 的指定中一定要包含逗號(不用小括號也可)或空集合 : ")
tuple_1 = (1)
print (type(tuple_1))
tuple_1 = (1,)
print (type(tuple_1))
tuple_1 = ()
print (type(tuple_1))
tuple_1 = 1,
print (type(tuple_1))
 
print ("\rtuple 算術運算子 (邏輯、比較、成員..運算子也可以 - 與 list 一樣) : ")
print (8*(8))
print (8*(8,))
 
print ("\rtuple 的修改(因為無法直接修改內容, 所以似重宣告一個) : ")
tuple_2 = ('A','B','C','D')
tuple_2 = tuple_2[:2] + ('BC',) + tuple_2[2:]
print (tuple_2)

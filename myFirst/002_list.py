# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:48:17 2017

@author: Administrator
"""


print ("\r列表裡的值可以是混合型態")
lst = ["A","B",12, ["AA","BB"],12.34]
print (lst)
print ("\rprint index 3 of list ([\"A\",\"B\",12,[\"AA\",\"BB\"]]) : ")
print (lst[3]);
print ("\rprint index [3][0] of list ([\"A\",\"B\",12,[\"AA\",\"BB\"]]) : ")
print (lst[3][0], len (lst[3][0]), 123, 0.00000000023, "Test1", "Test2");
 
print ("\rappend 一個值(\"E-C\") 到列表中: ")
lst.append("E-C")
print (lst)
 
print ("\rextend 列表 (合併二個列表) (lst.extent([\"Ext1\",\"Ext2\"])): ")
lst.extend(["Ext1", "Ext2"])
print (lst)
 
print ("\rinsert 一個值到列表的特定位置中 (lst.insert(1,\"Roy\"])): ")
lst.insert(1, "Roy")
print (lst)
 
print ("\rremove 某一個值 (\"B\") (lst.remove(\"B\")) : ")
lst.remove("B")
print (lst);
 
print ("\rdel 列表中的某一個元素值 (位置) (del lst[2]): ")
del lst[2]
print (lst)
 
print ("\rdelete all 命令為 (del lst)  (like clean as C#) : ")
 
print ("\r交換元素中的值 (先用暫存變數儲存 : ")
tempval = lst[1]
lst[1] = lst[0]
lst[0] = tempval
print (lst)
 
print ("\rpop value (從列表中 pop 最後一個->列表中值移出): ")
tempval = lst.pop()
print ("tempval=" + tempval)
print (lst)
print ("\rpop value (從列表中 pop 特定的位置->列表中值移出): ")
tempval = lst.pop(3)
print (lst)
 
print ("\rList 複製: ")
print (lst)
newlst = lst[:]
print (newlst)
newlst = lst[1:]
print (newlst)
newlst = lst[:3]
print (newlst)
newlst = lst[0:2]
print (newlst)
 
print ("\rList 比較大小 (從最小維度開始比, 只要能比出來就返回結果, 後面不再比): ")
lst_1 = [123,435]
lst_2 = [12, 23,345]
print (lst_1 > lst_2)
lst_3 = [123,435]
print (lst_1 > lst_2 and lst_1 == lst_3)
 
print ("\rList 運算: ")
print (lst_1 + lst_2)
print (lst_1 * 3)
lst_3 *= 5
print (lst_3)
print (123 not in lst_3)
print (12345 not in lst_3)
print ("AA" in lst[2])
 
print ("\r列出 list 的所有方法")
print (dir(list))
 
print ("\r列表的 count 方法")
print (lst_3.count(123))
print (lst_3.index(435))
print (lst_3.index(435, 3, 8))
lst.reverse()
print (lst)
print (lst_3)
lst_3.sort()
print (lst_3)
lst_3.sort(reverse=True)
print (lst_3)

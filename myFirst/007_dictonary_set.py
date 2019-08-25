# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:18:34 2017

@author: Administrator
"""

print ('dictonary 是唯一一種映射類型 (list, tuple .. 是序列類型')

print ('dictonary 用大刮號')
dic1= {'A':'很好','B':'好','C':'普通','D':'不好'}
print(dic1)
print (dic1['A'])

print ('dictonary index 可以是字串也可以是整數')
dic2= {1:'很好',2:'好',3:'普通',4:'不好'}
print(dic2)
print (dic2[2])


print('\n\n')
help(dict)
print ('\ndict(mapping) 的宣告方法')
dic3 = dict(((1,'前進'), (2,'後退'), (3,'靜止')))
print (dic3)
dic3 = dict(([1,'前進走'], [2,'後退走'], [3,'靜止不動']))
print (dic3)


print ('\ndict(**kwargs) 的宣告方法 (關鍵字參數宣告時, 索引不能加引號)')
dic4 = dict(我='皇佑', 他='默生人', 你='朋友')
print (dic4)
print ('指定元素值')
dic4['我'] = '皇佑變帥了'
print (dic4)
print ('指定元素值, 如果該元素(索引)找不到, 則會新增一個元素 (序列會報錯)')
dic4['其它'] = '怪物'
print (dic4)

print ('\ndictonary 函數 (fromkeys)')
dic1 = {}
print (dic1)
dic1 = dic1.fromkeys((1,2,3))
print (dic1)
dic1 = dic1.fromkeys((1,2,3),'xxx')
print (dic1)
print ('fromkeys 都會重新建立一個新的, 並不能修改已建立的值')
dic1 = dic1.fromkeys((1,2,3),('a','b','c'))
print (dic1)
print ('第二個參數的值是各項的預設值, 並沒有是 iterable 拆給各項的功能')
print (dic1.fromkeys((1,2),('aa')))

print ('\nkeys()')
dic1 = dic1.fromkeys(range(10),'YA')
for each in dic1.keys():
    print (each)
print (dic1.keys())
print ('\nvalues()')
for each in dic1.values():
    print (each)
print (dic1.values())
print ('\nitems()')
for each in dic1.items():
    print (each)
print (dic1.items())

print ('\nget()')
# print (dic1[10]) --> 找不到, 會錯
print (dic1.get(10))
print ('\n[找不到] 是索引不存在時會返回的預設值')
print (dic1.get(10,'找不到'))

print ('\n判斷索引存不存在')
print (10 in dic1)

print ('\nclear()')
dic1.clear()
print (dic1)
print ('\n直接指定變數為 {}, 可能資料還會存在記憶體中, 而 clear()不會')
dic1 = dic1.fromkeys(range(3), 'x')
print (dic1)
t = dic1
dic1 = {}
print (dic1)
print (t)


print (dir(dict))
print ('\ncopy()')
a = {1:'one',2:'two',3:'three'}
b = a.copy()
c = a
print ('以 id() 查過記憶體位置可以發現, copy() 的會另外建立新的, 指定的會指向同一位置')
print (id (a))
print (id (b))
print (id (c))
c[4] = 'four'
print (c)
print (a)
print (b)

print ('\npop() : 可指定位置取出')
print (a.pop(2))
print (a)
print ('popitme() : 因為 dictonary 編排是沒有順序的, 所以會隨機 pop 一個元素出來 (好像是有順序的, 取最後一個)')
print (a.popitem())
print (a)

a.setdefault('AAA')
print (a)
a.setdefault('BBB','NEWNEW')
print (a)
b = {'AAA':'Empty'}
a.update(b)
print (a)





print ('\n\nset 集合 (元素一定維, 元素內的值不可變更, 沒有一定位置順序')
print ('大刮號 {} 可以宣告 diconary 也可以宣告 set')
set1 = {}
print (type (set1))
set1 = {5,4,3,2,1}
print (type (set1))
print ('set 的值都是唯一')
set1 = {5,4,3,2,1,0,1,2,3}
print (set1)

print ('\nset() 函數宣告, 會被排序過')
set1 = set([3,2,1,2,3])
print (set1)

print ('\n二者的結果差在排序')
lst1 = [5,4,3,2,1,1,2,3]
lst2 = []
for each in lst1:
    if each not in lst2:
        lst2.append(each)
print (lst2)

lst2 = list(set(set1))
print (lst2)

print ('判斷存在與否')
print (1 in set1)
print ('1' in set1)

set1 = set([3,2,1,2,3])
print ('\nadd() (注意排序的問題)')
print (set1)
set1.add(2.5)
print (set1)
set1.add(4)
print (set1)
set1.remove(3)
print (set1)
print ('\nfor 列出')
for each in set1:
    print (each)


print ('\nfrozenset (不可變更元素 - add() / remove() )')
num = frozenset([2,1,3,5,4,3])
print (num)

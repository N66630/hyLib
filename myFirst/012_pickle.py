# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:22:22 2017

@author: Administrator
"""

import pickle
print ('\npickle 的 Picking : 將內容以二進制的方式存到硬碟 (任何型式的內容)')
my_list = [123,45.67,'中文',['Roy',28]]
pickle_file = open('pickle_file.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()


print ('\npickle 的 unPicking : 將二進制的檔案取出')
pickle_file = open('pickle_file.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
pickle_file.close()



import urllib.request
import json

file = urllib.request.urlopen('https://tw.stock.yahoo.com/q/q?s=6121')
stockHTML = file.read().decode('big5')
print (stockHTML)
# 下行有錯
#sotckJson = json.JSONDecoder().decode(stockHTML)

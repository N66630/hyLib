
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:20:20 2018

@author: Administrator
"""

#from xxx import * 不會import含有單底線的function 以避免汙染環境
#若想取用含底線的資源 import必須指明from underscore import [有底線 function name]
'''第一種 import 方法'''
from hyRoot.Common import CommVar 
from hyRoot.IO.Log import hyLog
from hyRoot.IO.Config import hyConfigBase
## o = CommVar()
import datetime

"""
測試取得 config / log path
"""
def test_getCommVar():
    print ('======== call the test_comVar() function ========')
    print ('## 宣告物件,會呼叫到 initi 的建構函數,其中會改變路徑 C:-> D: ')
    o = CommVar()
    print ('## 在雙底線變數前加上 class 名稱是可以取到的, 但建議不要這樣用, 如下會印出初始值而不是 init 中修改後的值 ')
    print (o._CommVar__APInfoPath)
    print ('## 雖然單底線的member我們可以自由的存取,但我們仍然不應該這樣做 ')
    print (o._APInfoPath)
    
    print ('## 方法一(一般普通): 因為是以 self 為操作目標, 所以路徑會是變更後的 D: ')
    print (o.get_APInfoPath_Obj())
    o.set_APInfoPath_Obj(r"D:"+'\\')
    print (o.get_APInfoPath_Obj())
    
    print ('## 方法二(類方法): 因為是以 cls 為操作目標, 所以路徑會是預設宣告的值 C: ')
    print (o.get_APInfoPath_Cls()) # cls._APInfoPath
    print (CommVar.get_APInfoPath_Cls_()) # cls.__APInfoPath
    print (CommVar.get_RootConfigPath_Cls())
    o.set_APInfoPath_Cls(r"E:"+'\\')
    print (CommVar.get_APInfoPath_Cls()) #因為上一行是改變 class 中的變收值, 所以這裡的值會是變更後的值
    
    print ('## 方法三(靜態方法)')          
    print (o.get_MaxLogFileSize())
    CommVar.set_MaxLogFileSize(19999)
    print (CommVar.get_MaxLogFileSize())

def test_writeLog():
    print ('======== call the test_writeLog() function ========')
    for num in range(50):
        #print (str(num)+'~'+"{:%Y%m%d_%H%M%S.%f}".format(datetime.datetime.now()))
        sc = str(num)+'~'+"{:%Y%m%d_%H%M%S.%f}".format(datetime.datetime.now())
        hyLog.writeLog("MyAP",funcname="myTest",text=sc)

def test_getConfig():
    print ('======== call the test_getConfig() function ========')
    print ('## 取得資料庫連線資訊')
    print (hyConfigBase.getDBConnectionString("3C","SiteDB"))   # ['L3CAPCDB01', '10.84.99.63', 'APC']
    print ('## 取得 DBUser_Admin 資訊')
    print (hyConfigBase.getAPCMainConfigText("//SystemInfo//DBUser_Admin")[0]) # [('InnerText', 'apc.sa')]
    print ('## 取得資料庫連線資訊')
    print (hyConfigBase.getAPCMainConfigText("//DBConnectionString//SiteDB"))   # [('InnerText', 'Data Source=AAAPC005;Database=APC;Pooling=true;'), [('User', 'apc.sa'), ('Test', 'Attrib_2')]]

   
if __name__ == '__main__':
    test_getCommVar()
    #test_writeLog()
    #test_getConfig()

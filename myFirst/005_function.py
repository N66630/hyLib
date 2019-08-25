# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:34:10 2017

@author: Administrator
"""

def MyFunc():
    return 'hello world'   
print (MyFunc())

def MyFunc2(name, age):
    'The name & age is parameter (形式參數), the name & age value is attribute (實際參數值). 以上在 function 開頭寫的字串, 就是 function 的說明'
    print ('hello ' + name + ', your age is ' + str(age))
MyFunc2('Roy', 28)

print ('\n取得函數的說明 1')
print (MyFunc2.__doc__)

print ('\n取得函數的說明 2')
print (help(MyFunc2))

print ('\n列出 print 的說明 (help() 會換行,顯示比較漂亮)')
print (print.__doc__)
print (help(print))

print ('\n關鍵數參數呼叫函數')
MyFunc2(age=28, name='Roy')


print ('\n有預數參數值的函數')
def MyFunc3(name='Roy', age=28):
    print ('hello ' + name + ', your age is ' + str(age))
MyFunc3()
MyFunc3('RoyLai')
MyFunc3(age=30)


print ('\n有params 關鍵數參數的函數 (*params 放在第一個, 呼叫時指定參數名)')
def MyFunc4(*params, name='Roy'):
    '*params 放在第一個, 呼叫時指定參數名)'
    print ('hello ' + name + ', your have friend as ' + str(list(params)))
MyFunc4('a','b','c','d')


print ('\n有params 關鍵數參數的函數 (*params 放在最後一個, 呼叫時指定參數名)')
def MyFunc4(name='Roy', age=28, *params):
    '*params 放在最後一個, 呼叫時指定參數名)'
    print ('hello ' + name + ', your age is ' + str(age) + ', and your have friend as ' + str(list(params)))
MyFunc4('roylai',29, 'b', 'c','d')

print ('\npython 只有 function 沒有 procedure, 所以都會返回值 (沒有則為 NoneType)')
temp = MyFunc4()
print (temp)
print (type(temp))
 
 
 
print ('\nfunction 返回多值 (集合)')
def MyFunc5(rtnItem):
    if rtnItem == 0:
        return [100, 'hello world', 12.34]
    else :
        return 1, 'hello', 45.66
print (MyFunc5(0))
print (MyFunc5(1))
 
print ('\n全域變數與區域變數的值')
def MyFunc6(name):
#    # 注意 : 如果這個函數皂最後二行不先 mark, 則下面這行會出現 UnboundLocalError: local variable .. 錯誤
#    #   因為 myname = 'Roy Lai 2222' 表示 myname 是這裡的區域變變, 但確還沒給它值, 所以會錯
#    print ('可以呼叫到外部的全域變數, myname=', myname)
    
    
#     myname = 'Roy Lai 2222'
#     print ('可以修改外部的全域變數 (注意:此處 python 會在函數內部建立一個同名的區域變數: shadowing 的方式保護全域變數), myname=', myname)
 
 
    global myname
    myname = 'Roy Lai 3333'
    print ('如果加上 global 的關鍵字告訴 python myname 真的是全域變數, 則修改就會真的變更, myname=', myname)
 
myname = 'Roy Lai' #input('input your name : ')
print (MyFunc6(myname))
print ('雖然呼叫 function 時, 在 function 內部有修改 myname 變數值, 但這裡不會改變, myname=', myname)
 
 
 
print ('\n全域變數與區域變數的值')
def MyFunc7(name):
    global myname
    myname = 'Roy Lai 3333'
    print ('如果加上 global 的關鍵字告訴 python myname 真的是全域變數, 則修改就會真的變更, myname=', myname)
 
myname = 'Roy Lai' #input('input your name : ')
print (MyFunc7(myname))
print ('因為 function 內部修改 myname 前有指定它是全域變數, 所以修改會真的實現, myname=', myname)
 
 
 
print ('\n巢狀函數 (因為 MyFuncInner() 被定義在 MyFuncOuter() 之內, 所以外部無法呼叫)')
def MyFuncOuter():
    print ('MyFuncOuter 被呼叫了')
    def MyFuncInner():
        print ('MyFuncInner 被呼叫了')
    print ('執行呼叫 MyFuncInner')
    MyFuncInner()
MyFuncOuter()
 
 
 
print ('\n巢狀函數中的內部函數稱為 Closure (閉包, 如 funcY)')
print ('函數可以回傳任何對象, 如此處 funcX 函數回傳了 funcY 函數')
def funcX(x):
    def funcY(y):
        return x*y
    return funcY
funcX
r = funcX(8)
print (type(r))
print (r(5))
print (funcX(8)(4))
 
 
 
print ('\n函數可以回傳任何對象, 此處 func1 會回傳 func2 的位置')
def func1():
    x = 5
    def func2():
        x *= x
        return x
    return func2  # 回傳 func2 的位置
print (func1())   # 此處 回傳 func2 的位置
# print (func1()())   # 會錯 : 因為在 func2 中的 x 未被定義 (它是上一層 func1 的變數)
print ('函數可以回傳任何對象, 此處 func1 會回傳 func2 的內容')
def func1():
    x = 5
    def func2():
        x *= x
        return x
    return func2()  # 回傳 func2 的內容
# print (func1())   # 會錯 : 因為在 func2 中的 x 未被定義 (它是上一層 func1 的變數)
print ('利用 nonlocal (因為 x 只是上一層 function 的變數而非 global 變數, 所以不能用 global)')
def func1():
    x = 5
    def func2():
        nonlocal x
        x *= x
        return x
    return func2()  # 回傳 func2 的內容
print (func1())
 
 
print ('\n匿名函數 (lambda)')
def ds(x):
    return 2 * x + 1
print (ds(5))
 
g = lambda x : 2 * x + 1
print (g)
print (g(5))
g = lambda x, y : x * y + 1
print (g(3,5))
 
 
 
print ('\nfilter() BIF 內建函數')
help(filter)
print ('如果第一個參數為 None, 則回傳第二個參數中為 true 的 iterable 元素)')
print ('如果第一個參數為 function, 則將第二個參數中的元素代入 function 的參數中, 回傳 true 的部分)')
# filter(function or None, iterable) --> filter object
print (list(filter(None, [1,0,'a',True, False,100,'true','false'])))
 
def odd(x):
    return x % 2
temp = range(10)
sort = filter(odd, temp)
print (list(temp))
print (list(sort))
 
print (list(filter(lambda x : x % 2, range(10))))
 
print ('\nmap() BIF 內建函數')
help(filter)
print ('如果第一個參數為 None, 則回傳第二個參數中為 true 的 iterable 元素)')
print ('如果第一個參數為 function, 則將第二個參數中的元素代入 function 的參數中, 回傳 true 的部分)')
# filter(function or None, iterable) --> filter object
print (list(filter(None, [1,0,'a',True, False,100,'true','false'])))
 
def odd(x):
    return x % 2
temp = range(10)
sort = filter(odd, temp)
print (list(temp))
print (list(sort))
 
print (list(filter(lambda x : x % 2, range(10))))
help(map)
print ('將第二個參數中的元素代入第一個參數的 function 中加工再輸出)')
print (list(map(lambda x : x*3, range(10))))

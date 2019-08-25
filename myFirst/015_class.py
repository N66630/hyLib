# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:11:58 2017

@author: Administrator
"""

print ('\nclass 用大寫字母開頭命名 (function 用小寫字母)')
class Turtle:
    #屬性
    color = 'green'
    weight = 23
    legs = 4
    
    #方法
    def climb(self):
        print ('我正在爬')
    def run(self):
        print ('我正在跑')
    def jump(self):
        print ('我正在跳')
        

print ('\nclass : 屬性、方法')
print ('OO物件導向 : 封裝、繼承、多型')
print ('實作 class 就會產生 object (object is class instance)')

print ('\n封裝 : ')
o = Turtle()
o.jump()

print ('\n繼承 : ')
class MyTurtle(Turtle):
    pass
o = MyTurtle()
o.climb()



print ('\nclass impletement (object)')
class Robot:
    def setName(self, name):
        self.name = name
    def run (self):
        print ('%s 開始在跑了' % self.name)
a = Robot()
a.setName('R1')
b = Robot()
b.setName('R2')
c = Robot()
c.setName('R3')
a.run()
c.run()


print ('\n建構函數 (__init__(self))')
class Robot:
    def __init__(self, name):
        self.name = name
    def run (self):
        print ('%s 開始在跑了' % self.name)
a = Robot('Robot1')
a.run()


print ('\npublic and private')
print ('屬性與方法都是 public')
class Person:
    name = 'Roy'
p = Person()
print (p.name)

print ('python 利用 namgling 技術處理私有變變 (在變數或函數前開頭加上 __ 即可)')
class Person:
    __age = 28
    name = 'Roy'
    def getAge(self):
        return self.__age
p = Person()
print ('無法得到私有變收的值 __age')
# print (p.__age) --> 會報錯
print ('利用 public 方法 (getAge) 取得 age')
print (str(p.getAge()))


print ('python 的 namgling 技術其實只是隱藏而已而不是真的的私有 (偽私有) (__ 其實是 _類別__變數)')
print (str(p._Person__age))






import random as r

print ('\n\n\n繼承時覆寫建構函數 (Shark 的覆寫了建構函數, 所以沒有 x, y 座標了, 執行 move() 函數會錯')
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0,10)
        
    def move (self):
        self.x -= 1
        print ('我目前的位置 : ', self.x, self.y)
        
class Goldfish(Fish):
    pass
class Garp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print ('好餓')
            self.hungry = False
        else:
            print ('好飽')
            self.hungry = True
fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
goldfish.move()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
shark.eat()
# shark.move() --> 會錯, 因為 Shark 的覆寫了建構函數, 所以沒有 x, y 座標了

print ('\n繼承時覆寫建構函數, 但同時保留父類建構函數中的部分')
print ('--> 調用未綁定的父類方法')
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0,10)
        
    def move (self):
        self.x -= 1
        print ('我目前的位置 : ', self.x, self.y)
        
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self) # 新增這行就可以保留父類的建構函數
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print ('好餓')
            self.hungry = False
        else:
            print ('好飽')
            self.hungry = True
shark = Shark()
shark.move() # 可以執行了
shark.move() # 可以執行了
shark.move() # 可以執行了


print ('\n繼承時覆寫建構函數, 也可以宣告完後, 將子類的 object 帶入父類的建構函數中, 以保留父類的建構函數工作')
print ('--> 調用未綁定的父類方法')
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0,10)
        
    def move (self):
        self.x -= 1
        print ('我目前的位置 : ', self.x, self.y)
        
class Shark(Fish):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print ('好餓')
            self.hungry = False
        else:
            print ('好飽')
            self.hungry = True
shark = Shark()
Fish.__init__(shark) # 也可以宣告完後, 將子類的 object 帶入父類的建構函數中
shark.move() # 可以執行了
shark.move() # 可以執行了
shark.move() # 可以執行了


print ('\n繼承時覆寫建構函數, 但可以利用 super() 同時保留全部父類建構函數中的部分')
print ('--> 使用 super() 函數')
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0,10)
        
    def move (self):
        self.x -= 1
        print ('我目前的位置 : ', self.x, self.y)
        
class Shark(Fish):
    def __init__(self):
        super().__init__() # 新增這行就可以保留父類的建構函數
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print ('好餓')
            self.hungry = False
        else:
            print ('好飽')
            self.hungry = True
shark = Shark()
shark.move() # 可以執行了
shark.move() # 可以執行了
shark.move() # 可以執行了


print ('\n\n多重繼承')
print ('class DerivedClassName(BVase1, Base2, Base3, ..) : ...')
class Base1:
    def foo1(self):
        print ('Base 1 foo 1')
class Base2:
    def foo2(self):
        print ('Base 2 foo 2')
class C(Base1, Base2):
    pass
c = C()
c.foo1()
c.foo2()


print ('\n\nPool')
class Bird:
    num 
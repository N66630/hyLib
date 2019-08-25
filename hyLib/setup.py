# -*- coding: utf-8 -*-

"""
如何製作可以傳到 PyPI (Python Package Index) 上面的專案:
    1. 在專案目錄下加入 README.md 檔案 : 用來介紹該專案的結構與使用方式
    2. 在專案目錄下加入 setup.py 檔案 : 用來安裝專案
    3. 在專案目錄下加入 .pipyrc 檔案 : 讓我們傳東西到PyPI上面
    4. 其它還可以在專案目錄下加入
        LICENSE, MANIFEST.in, requirements.txt, setup.cfg, test-requirements.txt, tox.ini ...
"""


"""
欄位名稱	描述
name	專案名稱(與專案目錄同名)
packages	要安裝的套件名稱
scripts	script名稱，通常代表一個執行檔，不一定有
version	版本
description	專案描述
author	作者
author_email	作者信箱
keywords	這個專案的一些關鍵字

#scripts :
    a.這邊要寫在scripts裡的是整個專案的執行檔，他可能用到了專案裡面的套件。為了要將該檔案同時也裝到使用者的系統上，我們需要把他也標註上去，否則後面我們利用pip安裝的時候就只會安裝package而不會安裝執行檔了。
    b.而這邊所謂對執行檔的安裝，其實也就是把指定的scripts放到一個可執行路徑裡，例如/usr/bin/中，如此使用者在安裝完後可在任何地方運行該script(其實我們能夠指定安裝的路徑，但如果只給script名稱，那他會被放在預設的位置)。
    c.這邊有一點一定要注意，script的名字千萬不要跟他要匯入的pakcage同名了，這會導致一些匯入上的失誤。
"""
#from distutils.core import setup
from setuptools import setup, find_packages

#NAME = 'hyRoot'
#PACKAGES = [NAME] + ["%s.%s" % (NAME, i) for i in find_packages(NAME)]
setup(
    name = 'hyLib',
    #底下這個方式只會包到根目錄而己,其它子目錄 package 不會封裝
    #packages = ['hyRoot','hyRoot.IO'], 
    # 不同方式可以封裝包含子目錄的 package
    #packages = PACKAGES, 
    packages=find_packages(where="hyRoot", include=("*")),#find_packages(exclude=["hyTests.*"]),
    include_package_data = True,
    #scripts = ['runner'],
    version = '3.6.1.0',
    description = 'Hyper Yield Project (Huang-Yu).',
    author = 'Huang-Yu',
    author_email = 'huangyu.lai@gmail.com',
    keywords = ['AUO','APC'],
    classifiers = [],
    url='https://github.com/the-gigi/hyLib',
    license='MIT Licence',
    #long_description=open('README.md').read(),
    #zip_safe=False,
    #setup_requires=['nose>=1.0'],
    #test_suite='nose.collector',
    platforms='any',
)
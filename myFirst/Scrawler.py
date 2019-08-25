import pandas as pd
import requests
from io import StringIO
import os
import sqlite3 
import time

def scrawler_test():
    res = requests.get("https://www.wibibi.com/info.php?tid=116")
    res.encoding = 'utf-8' # big5
    res.text
    f = open ("test.html", 'w', encoding='utf-8')
    f.write(res.text)
    f.close()
    
    dfs = pd.read_html('test.html')
    dfs[0]

def crawl_price():
    # 載入目標網頁中的內容 (利用 chrome F12 Network / header 取得 url (按下 button click), 再將 url 中的 json 替換為 csv -> 證券交易所有提供 csv)
    # 來源 (json/csv) : 證券交易所 / 交易資訊 / 盤後資訊 / 全部 (不含權證、牛熊證、可展延牛熊證 [查詢])
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20190808&type=ALLBUT0999&_=1565534783994"
    response = requests.get(url, 'utf-8')
    # 依 csv content row 取出
    lines = response.text.split('\n')
    # 宣告一變數, 用以數集要的資料集 (頁面中的前面資料不要)
    newlines = []
    for line in lines:
        #print (len(line.split('",')))
        # 經由觀察, 後面有 17 個欄位的資料才要, 所以將它們加入 newlines 中 --> 因為數字千位會有逗號, 所以要是 ", split
        if len(line.split('",')) == 17: 
            newlines.append(line)
    #newcontent = '\n'.join(newlines)
    #print(newcontent)
    # 將陣列用換行符號 join 成新的內容, 並觀察後將多餘的 '=' 號去除
    df = pd.read_csv(StringIO("\n".join(newlines).replace('=','')))
    # 因為會自動就換行, 所以指定其寬度, 讓同一 row 不要換行
    pd.set_option('display.width', 1000)
    #df.head()
    # 將 dataframe 全部轉為 string, 再將帽號去除
    df = df.astype(str)
    df = df.apply(lambda s: s.str.replace(',','')) # lambda 中 ':' 左邊為 input, 右邊為 output
    # 因為預設的 index 為序號是沒有意義的, 所以將 dataframe 的 index 設為有意義的 '證券代號'
    df = df.set_index('證券代號')
    #df.loc['0050']
    # 將每個 series 再轉為數值 (coerce 為如果轉換失敗, 則將其值設為 NaN 而不要報錯)
    df = df.apply(lambda s : pd.to_numeric(s, errors='coerce'))
    # 因為執行完上面之後, 連證券名稱都會變為 NaN (非數值), 所以利用底下找出非全部欄位全部的 row 都是 not number, 
    df = df[df.columns[df.isnull().sum() != len(df)]]
    #df.head()
    # 找收盤價比開盤價 5% 的股票
    df[df['收盤價'] / df['開盤價'] > 1.07]
    # 存成 csv
    filepath = 'D:/FileHistory/Store/20190808_price.csv'
    #print (filepath)
    df.to_csv(filepath, encoding='utf_8_sig')
    df = pd.read_csv(filepath, index_col='證券代號')
    # 排除數盤價為 (減號為去除的意思)
    df = df.loc[-df['收盤價'].isnull()]
    df.head()

def crawl_monthly_report():
    # 載入目標網頁中的內容 (利用 chrome F12 Network / header 取得 url (按下 button click), 再將 url 中的 json 替換為 csv -> 證券交易所有提供 csv)
    # 來源 (html): 公開資訊觀測站 / 彙總報表 / 資訊揭露 / 每月營收 / 採用IFRSs後營業收入彙總表 / 每月營業收入彙總表 [查詢]
    url = "https://mops.twse.com.tw/nas/t21/sii/t21sc03_106_1_0.html"
    response = requests.get(url)
    response.encoding = 'big5'
    dfs = pd.read_html(StringIO(response.text))
    df = dfs[0]
    # 因為欄位太多, 只取前面 20 個來看 --> 後來檢視後只有前面 10 個欄位有用
    #list(range(20)) # 此為產 0-19 的 list
    df = df[list(range(10))]
    # 找出第一個欄位為 '公司代號' 的第一個 row (第一個符合的 row), 再把該 row 的欄位指定為 df 的 columns
    df.columns = df[df[0] == '公司代號'].iloc[0]
    #df.head()
    # 將當月營收欄位非數值的 row 移除
    df = df.loc[-pd.to_numeric(df['當月營收'], errors='coerce').isnull()]
    # 將公司代號欄位中為 '合計' 的 row 移除
    df = df.loc[-(df['公司代號'] == '合計')]
    # 設定 df 的 index, 不要用序號當 index
    df = df.set_index(['公司代號','公司名稱'])
    # 將欄位轉為數值, 無法轉的保留原值
    df = df.apply(pd.to_numeric)
    #df
    filepath = 'D:/FileHistory/Store/10601_monthly_report.csv'
    #print (filepath)
    df.to_csv(filepath, encoding='utf_8_sig')
    df = pd.read_csv(filepath, index_col=['公司代號','公司名稱'])
    df.head()

    ### 儲存到 sqlite3
    # 連接資料庫檔案
    conn = sqlite3.connect('D:/FileHistory/Store/test.sqlite3')
    df.to_sql('monthly_report', conn, if_exists='replace')

    df = pd.read_sql('select * from monthly_report', conn, index_col=['公司代號','公司名稱'])
    df
    ###

def finance_season_download(sid, year, season):
    #res = requests.get("https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=1101&SYEAR=2017&SSEASON=3&REPORT_ID=C")
    res = requests.get("https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID="+sid+"&SYEAR="+year+"&SSEASON="+season+"&REPORT_ID=C")
    res.encoding = "big5"
    filepath = 'D:/FileHistory/Store/' + sid + '_' + year + '_' + season + '.html'
    f = open(filepath, 'w')
    f.write(res.text)
    f.close()
    time.sleep(3) # 休息3秒
    #res.text[:2000]
    #pds = pd.read_html(StringIO(res.text))
    #pds[0]
def finance_season_read(sid, year, season):
    dfs = []
    filepath = os.path.join('D:', 'FileHistory', 'Store', sid + '_' + year + '_' + season + '.html')
    print( filepath)
    dfs.append(pd.read_html(filepath, encoding='big5'))
    print (dfs[0])

    
if __name__ == '__main__':
    #scrawler_test()
    #crawl_price()

    #sid = ['1001','2330']
    #year = ['2018']
    #season = ['1','2','3','4']
    #for id in sid:
    #    for y in year:
    #        for s in season:
    #            finance_season_download(id, y, s)
    finance_season_read('2330','2018','3')

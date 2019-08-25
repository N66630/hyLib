import sys
import os
#import ConfigParser --> python 2
import configparser 

if __name__ == '__main__':
    #scrawler()
    crawl_price()

    ###

    #取得 ini file path (目前file同路徑下)
    #region
    currentPath = os.path.dirname(os.path.realpath(__file__))
    cnfPath = os.path.join(currentPath, 'config.ini')
    '''print ('我的 ini 檔名稱 : ' + cnfPath)'''
    #endregion

    #創建管理對象
    _cf = configparser.ConfigParser()
    #讀取 ini 檔
    _cf.read(cnfPath, encoding='utf-8')
    #取得所有的 session
    sessions = _cf.sections()
    '''print(sessions) # return list'''
    #取得某 session 下的 items
    '''
    session_0_items = _cf.items(sessions[0])
    session_1_items = _cf.items(sessions[1])
    print (session_0_items)
    print dict(session_1_items)['process_no_unitid']
    '''

    try:
        inputfile = "D:/AP Backup/Roy/xgBoostData/7B AS Remain/file2/Data_Duplicate.csv"
        #讀取檔案
        dfs = pd.read_csv(inputfile)
        #print (dfs)
        #dfs["C"].astype(float)
        #dfs = dfs.drop_duplicates()
        #print (dfs)
    except FileNotFoundError:
        print('檔案不存在嗎?')
        #sys.exit("error")
        os._exit(0)

    nunique = dfs.apply(pd.Series.nunique)
    iClassNum = int(nunique[strClassColumn])
    cols_to_drop = nunique[nunique == 1].index
    cols_to_drop = [s for s in cols_to_drop if s not in lsExcludeColumns]
    dfs.drop(cols_to_drop, axis=1)

    #處理沒有UNIT_ID (每個 file 逐一執行)
    if bool(_cf.get('ProcessConfig','process_no_unitid')) == True:
        sourcePath = _cf.get('BasicInfo','SourcePath')
        #filename = filter(os.path.isfile, os.listdir(sourcePath))
        filename = [f for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, f))]
        for i in range(len(filename)):
            file = filename[i]
            Process_Without_UNIT_ID(sourcePath + file, sourcePath + 'output/' + file)
    ###
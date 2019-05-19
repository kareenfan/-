# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 0:18
# @Author  : fanjj09512
# @File    : setting.py
# @Software: PyCharm
import re
import pandas as pd

#翻译相关的字典
def remhtml(dataframe, column):
    # 剔除HTML标签
    regex = re.compile(r'<.*?>', re.S)
   # print('剔除前',dataframe[column])
    dataframe[column].replace(regex, '', inplace=True)
   # print('剔除后',dataframe[column])
    regex = re.compile(r'&nbsp;')
    dataframe[column].replace(regex, ' ', inplace=True)
    regex = re.compile(r'&lt;')
    dataframe[column].replace(regex, '<', inplace=True)
    regex = re.compile(r'&gt;')
    dataframe[column].replace(regex, '>', inplace=True)
    regex = re.compile(r'&amp;')
    dataframe[column].replace(regex, '&', inplace=True)
    regex = re.compile(r'&quot;')
    dataframe[column].replace(regex, '"', inplace=True)
    regex = re.compile(r'&copy;')
    dataframe[column].replace(regex, '@', inplace=True)
    return dataframe

    # 翻译转义字符
'''
    regex = re.compile(r'&nbsp;')
    dataframe[column].replace(regex, ' ', inplace=True)
    regex = re.compile(r'&lt;')
    dataframe[column].replace(regex, '<', inplace=True)
    regex = re.compile(r'&gt;')
    dataframe[column].replace(regex, '>', inplace=True)
    regex = re.compile(r'&amp;')
    dataframe[column].replace(regex, '&', inplace=True)
    regex = re.compile(r'&quot;')
    dataframe[column].replace(regex, '"', inplace=True)
    regex = re.compile(r'&copy;')
    dataframe[column].replace(regex, '@', inplace=True)
'''


#获取工号和姓名
def getDict(idPath,fundction):
    if fundction =='testdesc':
        iddf = pd.read_excel(idPath, dtype={'id': str, 'name': str})
        idlist = list(iddf['id'])
        namelist = list(iddf['name'])
        nvs = zip(idlist, namelist)
        return dict((id, name) for id, name in nvs)
    if fundction =='testResult':
        iddf = pd.read_excel(idPath, dtype={'testResult':str,'testResultdesc':str})
        idlist = list(iddf['testResult'])
        namelist = list(iddf['testResultdesc'])
        nvs = zip(idlist, namelist)
        return dict((id, name) for id, name in nvs)
    if fundction =='modifyStatus':
        iddf = pd.read_excel(idPath, dtype={'modifyStatus':str,'modifyStatusdesc':str})
        idlist = list(iddf['modifyStatus'])
        namelist = list(iddf['modifyStatusdesc'])
        nvs = zip(idlist, namelist)
        return dict((id, name) for id, name in nvs)
    if fundction =='productId':
        iddf = pd.read_excel(idPath, dtype={'productId': str, 'productIddesc': str})
        idlist = list(iddf['productId'])
        namelist = list(iddf['productIddesc'])
        nvs = zip(idlist, namelist)
        return dict((id, name) for id, name in nvs)



#一个修改单多测试执行人工号和姓名
def mulreplace(dataframe, column ,dict):
    #print(dataframe[column].size)
    for i in range(0, dataframe[column].size):
        #a = dataframe.loc[i, [column]]
        #print('试试',a)
        #print('计数：',i)
        if str(dataframe.loc[i, [column]]).find(',') > -1:
            temp = list(dataframe.loc[i, [column]])[0].split(',')
           # print('temp', temp)
            #temp,翻译字典和名字
            temp = [dict[x] if x in dict else x for x in temp]
            #print('翻译后的值', temp)
            dataframe.loc[i, [column]] = ','.join(temp)
    return dataframe

'''
if __name__=="__main__":
    idPath = 'F:\pythonwork\字典表.xlsx'
    aa = getDict(idPath,'testdesc')
    print(aa)
    bb = [{'tester': '24791'}, {'tester': '25491,25499'}]
    df = pd.DataFrame(bb)
    print(df)
    testerdict = getDict(idPath,'testdesc')
    cc = mulreplace(df, 'tester' ,testerdict)
    print(cc['tester'])
'''









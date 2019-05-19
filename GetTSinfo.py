# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 21:36
# @Author  : fanjj09512
# @File    : GetTSinfo.py
# @Software: PyCharm

import requests
import re
import json
import time
import pandas as pd

#TS登陆和获取数据
def GetTSinfomation(searchurl, tsparam, username, password, FILEpath):
    print('开始登陆TS系统')
    #1.获取登陆链接
    session = requests.session()
    get = session.get('https://ts.hundsun.com/se')
    url = get.url
    text = get.text
    lt = re.findall('name="lt" value="(.*?)" />', text)[0]
    execution = re.findall('name="execution" value="(.*?)" />', text)[0]
    #print(lt)
    #print(execution)
    data = {"username": username,
            "password": password,
            "lt": lt,
            "execution": execution,
            "_eventId": "submit",
            "submit": ""
            }
    #2.登陆中
    a = session.post(url, data)
    #3.访问登陆后界面，获取token等值
    print('获取登陆后相关内容')
    ts = session.get('https://ts.hundsun.com/se/portal/SupportPortal.htm')
    # print(ts.content.decode())
    token = re.findall('se.SEConfig.token = "(.*?)";', ts.text)[0]
    #print('token值：', token)
    currentgroup = re.findall('se.SEConfig.currentGroup			= "(.*?)";', ts.text)[0]
    #print('currentgroup:', currentgroup)
    pennanter = re.findall('se.SEConfig.pennanter               = "(.*?)";', ts.text)[0]
    UserId = re.findall('se.SEConfig.UserId			= "(.*?)";', ts.text)[0]
    #print('pennanter', pennanter)
    #4.一个认证登陆
    data = {
        'userId':UserId,
        'sourceId':'CLIENT',
        'groupId': currentgroup,
        'productIds':'20100101,20100702,20131001,20140202,20140805,20140806,20150209,20160112,20100202,20150326,20100901,20160404,20170203,20100201,20091108,20110301,20120403,20160502,20170202,20091109,20131101,20100316,20161108,20130805',
        'currentGroup': currentgroup,
        'token': token
    }
    session.post('https://ts.hundsun.com/se/userGroup/UserGroupAction.htm', data)
    #print('session.post', session.post)
    data1 = {
        'userId':UserId,
        'sourceId':'USERROLES',
        'groupId': currentgroup,
        'productIds':'20100101,20100702,20131001,20140202,20140805,20140806,20150209,20160112,20100202,20150326,20100901,20160404,20170203,20100201,20091108,20110301,20120403,20160502,20170202,20091109,20131101,20100316,20161108,20130805',
        'currentGroup': currentgroup,
        'token': token
    }
    session.post('https://ts.hundsun.com/se/userGroup/UserGroupAction.htm', data1)
    #print('session.post1', session.post)
    data2 = {
        'userId':UserId,
        'sourceId':'CLIPRO',
        'groupId': currentgroup,
        'productIds':'20100101,20100702,20131001,20140202,20140805,20140806,20150209,20160112,20100202,20150326,20100901,20160404,20170203,20100201,20091108,20110301,20120403,20160502,20170202,20091109,20131101,20100316,20161108,20130805',
        'currentGroup': currentgroup,
        'token': token
    }
    session.post('https://ts.hundsun.com/se/userGroup/UserGroupAction.htm', data2)
    #print('session.post2', session.post)
    print('登陆成功，开始抓数据')

    #5.准备抓取数据，入参tsparam
    #tsparam = {"productId":"","modifyNum":"","bugNum":"","reqNum":"","taskNum":"","patchNum":"","modifyStatus":"","relationModifyNum":"","relationType":"","completedStatus":"","taskType":"","phase":"","isProgramArchive":"","extTxt7":"","createDate":"","createDate2":"","createDateCondition1":"","createDateCondition2":"","modifyType":"","customername":"","onlineTest":"","screenCollator":"2","publicPortion":"","modifyDifficulty":"","modifyPriority":"","receiver":"","testAssigner":"","tester":"","integationMan":"","auditor":"","modifier":"","verifier":"","testType":"","testSuggestion":"","testResult":"","testModifyType":"","integationCallBackReason":"","testCallBackReason":"","testStyle":"","auditingResult":"","auditBackReason":"","verifyResult":"","verifyDate":"","verifyDate2":"","verifyDateCondition1":"","verifyDateCondition2":"","verifyBackTimes":"","verifyBackTimes2":"","promiseDate":"","promiseDate2":"","promiseDateCondition1":"","promiseDateCondition2":"","integationDate":"","integationDate2":"","integationDateCondition1":"","integationDateCondition2":"","modifyDate":"","modifyDate2":"","modifyDateCondition1":"","modifyDateCondition2":"","testAccomplishDate":"","testAccomplishDate2":"","accomplishDateCondition1":"","accomplishDateCondition2":"","commitDate":"","commitDate2":"","commitDateCondition1":"","commitDateCondition2":"","lastCommitDate":"","lastCommitDate2":"","lastCommitDateCondition1":"","lastCommitDateCondition2":"","testDate":"","testDate2":"","testDateCondition1":"","testDateCondition2":"","archDate1":"","archDate2":"","archDateCondition1":"","archDateCondition2":"","versionNo":"","extTxt8":"","moduleName":"","packageName":"ETS_4.2.5.0.0-TPJJ","returnCount":"","returnCount2":"","modifyFile":"","modifyReason":"","modifyDesc":"","modifySummary":"","memo":"","outProgram":""}
    tsparam = json.dumps(tsparam)
    #print(tsparam)
    searchurl = 'https://ts.hundsun.com/se/services/modify/fetchModifyByUserdefinedModluePaginated.htm?_dc='
    url = searchurl + str(int(round(time.time() * 1000))) + ""
    #print(url)
    data3 = {
        "param": tsparam,
        "start": '0',
        "limit": "400",
        "pennanter": pennanter,
        "isUserDataValidity": 'Y',
        "page": '1',
        "currentGroup": currentgroup,
        "token": token
    }
    search = session.post(url, data3)
    searchresult = search.text
    searchresult = json.loads(searchresult)
    searchresult = searchresult.get('resultBOList')
    df = pd.DataFrame(searchresult).fillna('')
    #print(searchresult)
    #6.导出结果
    excel = pd.ExcelWriter(FILEpath)
    df.to_excel(excel, 'Sheet1')
    print('TS获取修改单完成')
    return df
'''
if __name__=="__main__":
    searchurl = 'https://ts.hundsun.com/se/services/modify/fetchModifyByUserdefinedModluePaginated.htm?_dc='
    aa = GetTSinfomation(searchurl)
    #print(aa)
'''
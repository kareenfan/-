# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 18:51
# @Author  : fanjj09512
# @File    : ts_test.py
# @Software: PyCharm
import xlsxwriter
import os
import GetTSinfo
import setting
def modifywt(report, testPackageName, username, password, idPath, FILEpath):
    print('创建excel中修改单tab页')
    modify = report.add_worksheet('包含修改单')
    # 调整宽度
    modify.set_column(0,5,15)
    searchurl = 'https://ts.hundsun.com/se/services/modify/fetchModifyByUserdefinedModluePaginated.htm?_dc='
    # print(searchurl)
    tsparam = {"productId":"","modifyNum":"","bugNum":"","reqNum":"","taskNum":"","patchNum":"","modifyStatus":"","relationModifyNum":"","relationType":"","completedStatus":"","taskType":"","phase":"","isProgramArchive":"","extTxt7":"","createDate":"","createDate2":"","createDateCondition1":"","createDateCondition2":"","modifyType":"","customername":"","onlineTest":"","screenCollator":"2","publicPortion":"","modifyDifficulty":"","modifyPriority":"","receiver":"","testAssigner":"","tester":"","integationMan":"","auditor":"","modifier":"","verifier":"","testType":"","testSuggestion":"","testResult":"","testModifyType":"","integationCallBackReason":"","testCallBackReason":"","testStyle":"","auditingResult":"","auditBackReason":"","verifyResult":"","verifyDate":"","verifyDate2":"","verifyDateCondition1":"","verifyDateCondition2":"","verifyBackTimes":"","verifyBackTimes2":"","promiseDate":"","promiseDate2":"","promiseDateCondition1":"","promiseDateCondition2":"","integationDate":"","integationDate2":"","integationDateCondition1":"","integationDateCondition2":"","modifyDate":"","modifyDate2":"","modifyDateCondition1":"","modifyDateCondition2":"","testAccomplishDate":"","testAccomplishDate2":"","accomplishDateCondition1":"","accomplishDateCondition2":"","commitDate":"","commitDate2":"","commitDateCondition1":"","commitDateCondition2":"","lastCommitDate":"","lastCommitDate2":"","lastCommitDateCondition1":"","lastCommitDateCondition2":"","testDate":"","testDate2":"","testDateCondition1":"","testDateCondition2":"","archDate1":"","archDate2":"","archDateCondition1":"","archDateCondition2":"","versionNo":"","extTxt8":"","moduleName":"","packageName":testPackageName,"returnCount":"","returnCount2":"","modifyFile":"","modifyReason":"","modifyDesc":"","modifySummary":"","memo":"","outProgram":""}
    # print(type(searchurl))
    modifydata = GetTSinfo.GetTSinfomation(searchurl,tsparam,username,password,FILEpath)
    # 翻译相关字典
    print('字段转义开始')
    testResultdesc = setting.getDict(idPath,'testResult')
    modifystatusdict = setting.getDict(idPath,'modifyStatus')
    #翻译
    testerdict = setting.getDict(idPath,'testdesc')
    # print('看看字典：', testerdict)
    modifydata['tester'].replace(testerdict, inplace=True)
    # print('转义后tester', modifydata['tester'])
    modifydata = setting.mulreplace(modifydata, 'tester', testerdict)
    # print('转义后2tester', modifydata['tester'])
    modifydata['testResult'].replace(testResultdesc, inplace=True)
    modifydata['modifyStatus'].replace(modifystatusdict, inplace=True)
    modifydata = setting.remhtml(modifydata, 'modifyDesc')
    # print('转义后',modifydata['modifyDesc'])
    print('字段转义完成')
    modifydata = list(modifydata[['reqNums', 'modifyNum', 'modifyDesc',
                                  'tester', 'testResult', 'modifyStatus']].values)
    linecount = len(modifydata)+1
    arr = "A1:F%d" % linecount
    columns = [{'header': '需求编号'}, {'header': '修改单编号'}, {'header': '修改内容'}, {'header': '测试人员'}, {'header': '测试结果'},
               {'header': '修改单状态'}]
    modify.add_table(arr, {'data': modifydata,'autofilter': False, 'columns': columns, 'style': 'Table Style Light 9'})
    print('导出到excel完成')
    #print(type(modifydata))

if __name__=="__main__":
    try:
        # searchurl = 'https://ts.hundsun.com/se/services/modify/fetchModifyByUserdefinedModluePaginated.htm?_dc='
        # aa = GetTSinfo.GetTSinfomation(searchurl)
        # print(aa)
        print('本程序经不起暴力，有问题请联系范佳郡')
        print('配置字典文件默认在F盘根目录')

        print('开始创建导出文件TS.xlsx，默认在F:\TS.xlsx，可自己指定')
        idPath = 'F:\dictiaonary.xlsx'
        FILEpath = input("请指定导出的excel路径和名称（格式样式：F:\TS.xlsx）：")
        if FILEpath == '':
            FILEpath = 'F:\TS.xlsx'  # 定义文件路径
        if os.path.exists(FILEpath):
            os.remove(FILEpath)
        report = xlsxwriter.Workbook(FILEpath)
        testPackageName = input("请输入测试包版本号： ")
        username = input("请输入登陆TS的域账号：")
        password = input("请输入登陆TS的域账户密码: ")
        print('程序开始跑起来了')
        modifywt(report, testPackageName, username, password, idPath, FILEpath)
        report.close()
        print('导出成功，感谢体验')
    except:
        print('报错了，请联系范佳郡')


# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-15 09:27  
# software  :python_learn 

from www.element_operate import ElementOperate
from www.excel_operate import DealXlsElement
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#打开到默认任务单
class Login():
    def __init__(self,isdisplay):
        self.isdisplay=isdisplay
        # 隐藏浏览器
        if isdisplay=='是':
            # 显示浏览器
            browser = webdriver.Chrome()
            browser.maximize_window()
            self.browser=browser
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.maximize_window()
            self.browser = browser
    def login(self):
        print("开始登录TS，加载初始化参数！")
        try:
            self.browser.get('https://ts.hundsun.com/se/portal/SupportPortal.htm')
            self.browser.implicitly_wait(30)
            wait = WebDriverWait(self.browser, 10)
            # 加载EXCEL表格
            InputElement = DealXlsElement('任务单分配参数').dealxlselement('dict',1)
            elementObj = wait.until(EC.presence_of_element_located((By.XPATH, InputElement.get('用户名元素'))))
            elementObj.send_keys(InputElement.get('用户名'))
            elementObj = wait.until(EC.presence_of_element_located((By.XPATH, InputElement.get('密码元素'))))
            elementObj.send_keys(InputElement.get('密码'))
            ElementOperate(self.browser, InputElement).clickwait('提交按钮元素')
            print('TS登录成功！')
            # 点击任务管理按钮
            try:
                ElementOperate(self.browser, InputElement).clickwait('任务管理按钮元素')

            except:
                print('点击任务管理按钮异常！')
                self.browser.close()
            print('任务管理操作界面加载成功！')
            return self.browser
        except TimeoutException as e:
            print('TS登录报错，请校验用户名，密码是否正确！！！')



if __name__ == "__main__":
    InputElement = DealXlsElement('任务单分配参数').dealxlselement('dict',1)
    # browser = Login(InputElement.get('是否打开浏览器')).login()

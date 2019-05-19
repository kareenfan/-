# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-15 09:38  
# software  :python_learn 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class ElementOperate():
    def __init__(self,browser,InputElement):
        self.InputElement=InputElement
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
    def click(self,name):
        elementObj = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.InputElement.get(name))))
        elementObj.click()

    def waittime (self):
        time.sleep(int(self.InputElement.get('强制等待时间')))

    def clickwait(self,name):
        elementObj = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.InputElement.get(name))))
        elementObj.click()
        self.waittime()

    def inputmsg(self,name,msg):
        elementObj = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.InputElement.get(name))))
        elementObj.click()
        elementObj.clear()
        elementObj.send_keys(msg)
        elementObj.send_keys(Keys.ENTER)


    def clear(self,name):
        elementObj = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.InputElement.get(name))))
        elementObj.click()
        elementObj.clear()
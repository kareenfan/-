# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019/8/4
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import pymysql

driver = webdriver.Chrome()
# 设置网站最大响应时间
wait = WebDriverWait(driver, 50)

class TaoBaoSearch:
    # 初始化，默认搜索为None，创建数据库连接
    def __init__(self, search=None):
        self.name = search
        #self.mysql = to.Data_oper()
        print('看看',self.name)

    def search(self):
        # J_TSearchForm > div.search-button > button
        driver.get("https://www.taobao.com/")#J_TSearchForm > div.search-button > button
        # “q”为淘宝首页输入框的标签，这里定位到该输入框，并设置要搜索商品的名字

        imput = driver.find_element_by_id("q")
        imput.send_keys(self.name)
        # 点击搜索，实际场景需要手动再登陆下
        a = driver.find_element_by_css_selector('#J_TSearchForm > div.search-button > button')
        a.click()

        # wait.until()该方法的作用是加载出来搜索结果总页数之后开始往下执行,拷贝页数JS Path
        # 实际场景还需要手动刷新下
        pageText=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        total = re.search("\d+", pageText.text)
        # 该方法返回搜索结果的总页数
        return total.group(0)
# 提取出相应的数据
    def parseHtml(self):
        # 获取网页源码
        html = driver.page_source
        doc = qp(html)


if __name__ == '__main__':
    a = TaoBaoSearch(search='钱包').search()
    print(a)

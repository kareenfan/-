# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-04 22:50  
# software  :python_learn 
from urllib import request
import chardet

if __name__ == '__main__':
    # 下载一个网页并解码
    url = 'http://www.dangdang.com/'
    rsp = request.urlopen(url)
    html = rsp.read()
    print("URL： {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    # 自动获取网页的编码方式方便解码
    cs = chardet.detect(html)
    print('cs的属性:{0}'.format(cs))
    # html = html.decode('gbk')
    # 使用get取值保证不会出错,能取到则取对应的编码，取不到则使用utf-8
    html = html.decode(cs.get('encoding', 'utf-8'))
    # print(html)


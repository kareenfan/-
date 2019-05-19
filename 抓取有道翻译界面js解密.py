# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-19 11:05  
# software  :python_learn 

from urllib import request, parse
import time, random
'''
通过查找，能找到js代码中操作代码
1. 这个是计算salt的公式 salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2. sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE");
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是。。。。。
第二个参数就是输入的要查找的单词
'''

def getsalt():
    # salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
    salt = int(time.time()*1000 + random.randint(0, 10))
    print('得到的salt的值是:{0}'.format(salt))
    return salt

def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要一共bytes格式的参数
    md5.update(v.encode())
    sign = md5.hexdigest()
    print(sign)
    return sign


def getsign(key, salt):
    # sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE");
    print(key)
    print(salt)
    sign = 'fanyideskweb'+ key + str(salt) + '@6f#X3=cCuncYssPsuRUE'
    sign = getmd5(sign)
    print('使用的salt的值：{0}'.format(salt))
    print('得到的sign的值是：{0}'.format(sign))
    return sign


def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = getsalt()
    sign = getsign(key, salt)
    ts = int(time.time()*1000)
    print('ts的值：{0}'.format(ts))
    print(type(ts))
    bv = getmd5('5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')
    print('bv的值：{0}'.format(bv))
    print(type(bv))

    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data = parse.urlencode(data).encode()
    headers = {

        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh; q=0.9, en; q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': len(data),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=279176216@10.169.0.84; JSESSIONID=aaar94r8e6Fw_6qs76nRw; OUTFOX_SEARCH_USER_ID_NCOO=2042718013.0744262; ___rl__test__cookies=1558235195620',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    req = request.Request(url=url, data=data, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    print(html)


if __name__ == '__main__':
    youdao('boy')
    # salt = getsalt()
    # getsign('girl',salt)
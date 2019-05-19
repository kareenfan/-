# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-04 22:50  
# software  :python_learn 
from urllib import request, parse, error
import chardet
import ssl
import json
import requests
from http import cookiejar

def htmlfanyi(url,kw):
    try:
        # 使用data，将需要的值使用字典结构编写
        data ={
            'kw': kw
        }
        # 对关键词进行编码，只有编码后才能识别
        data = parse.urlencode(data).encode()
        print('编码后输入的关键词的内容：{0}'.format(data))


        # ssl加密
        ssl._create_default_https_context = ssl._create_unverified_context
        # context = ssl._create_unverified_context()
        '''
        # 方法1：使用urlopen来处理请求
        # 增加入参，翻译网址为
        rsp = request.urlopen(url=url, data=data, context=context)
        '''
        # 方法2：使用Request来处理请求，需要header
        # header中用户代理，简称UA， 属于heads的一部分，服务器通过UA来判断访问者身份,设置UA可以通过两种方式,header方式1
        headers = {
            'Content-Length': len(data),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
        rsp = request.Request(url=url, data=data, headers=headers)
        # header方式2：add_header
        rsp.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
        # 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
        rsp = request.urlopen(rsp)



        # 读传入入参后的html网页
        json_data = rsp.read().decode()
        print(type(json_data))
        # 把json字符串转化成字典
        json_data = json.loads(json_data)
        print(json_data)
        # 打印对应的关键词和翻译值
        for item in json_data['data']:
            print(item['k'], '----', item['v'])

    # HTTPError是对应的HTTP请求的返回码错误, 如果返回错误码是400以上的，则引发HTTPError
    except error.HTTPError as e:
        print('HttpError:{0}'.format(e))
    # URLError对应的一般是网络出现问题，包括url问题
    except error.URLError as e:
        print('UrlError:{0}'.format(e))

    except Exception as e:
        print('捕捉后的错误是：{0}'.format(e))
    # 关系区别从大到小： OSError-URLError-HTTPError

def htmlfinder(url,wd):
    print('hhaa')
    # 要想使用data， 需要使用字典结构
    wd = {
        'wd': wd
    }

    # 转换url编码
    wd = parse.urlencode(wd)
    print(wd)

    fulurl = url + wd
    print('拼接后的网址:{0}'.format(fulurl))

    # 如果直接用可读的带参数的url，是不能访问的
    #fullurl = 'http://www.baidu.com/s?wd=大熊猫'
    # 直接搜索的网址为
    rsp = request.urlopen(fulurl)
    html = rsp.read()
    # 打印url相关信息
    print("URL： {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    # 自动获取网页的编码方式方便解码并打印网页
    cs = chardet.detect(html)
    print('cs的属性:{0}'.format(cs))
    # 使用get取值保证不会出错,能取到则取对应的编码，取不到则使用utf-8
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)

def htmlproxy(url):
    # 基本使用步骤(4步)：获取代理服务器的地址：www.xicidaili.com  www.goubanjia.com
    # 设置代理地址
    proxy = {'http':'58.253.154.109:9999'}
    # 创建ProxyHandler
    proxyhandler = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxyhandler)
    # 安装Opener
    request.install_opener(opener)
    try:
        rsp = request.urlopen(url=url)
        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)

def htmllogin_session():
    # res = requests.post('http://nladuo.cn:90/crawler_lesson2/do_login.php', data={'uname':'nladuo','passwd':'nladuo'})
    # res = requests.get('http://nladuo.cn/crawler_lesson2/private.php')
    # res.encoding ='utf-8'

    # 使用session来进行访问
    # 创建一个session
    session = requests.session()
    res = session.post('http://nladuo.cn:90/crawler_lesson2/do_login.php',
                        data={'uname': 'nladuo', 'passwd': 'nladuo'})
    res = session.get('http://nladuo.cn/crawler_lesson2/private.php')
    res.encoding = 'utf-8'

    if res.status_code == 200:
        print(res.text)


def htmllogin_cookie():
    '''
    # 方式1，手动获取cookie登陆
    url = 'http://www.renren.com/290945236/profile'
    # 从网址f12中获取登陆的cookie
    hearders = {
        'Cookie':'anonymid=jvt2qxshui2rua; depovince=GW; jebecookies=a7626a85-b224-4e30-b3d7-c12e67e2d4d4|||||; _r01_=1; JSESSIONID=abc4xyp-gRZi56QnlBjRw; ick_login=c056991b-81dd-44e0-be54-2aec7fb061f9; _de=CBC1F09DABF094CB727E6F614F21270D; p=91eb1d36eb38e1dac3c292228f0985ed6; first_login_flag=1; ln_uact=18767101020; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20111005/1700/h_main_Snnk_2095000200b32f75.jpg; t=eeb3b8930db21a2690b5473b65a06ad36; societyguester=eeb3b8930db21a2690b5473b65a06ad36; id=290945236; ver=7.0; jebe_key=c21984c4-e831-41c9-9a55-0cd1f195b183%7Cdbdf9d3356b37bca42cf2586a2a96f51%7C1558157549546%7C1%7C1558157549601; wp_fold=0; xnsid=36927821; loginfrom=null'
    }

    rsp = request.Request(url=url,headers=hearders)
    rsp = request.urlopen(rsp)
    html = rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)
    '''
    # 方式2：自动获取cookie登陆的流程：
    # 创建cookiehar实例
    # 方式1：使用cookiejar
    cookie = cookiejar.CookieJar()
    # 方式2：创建filecookiejar实例
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    # 生成cookie的管理器
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 创建http的管理器
    http_handler = request.HTTPHandler()
    # 生成https的管理器
    https_handler = request.HTTPSHandler()
    # 创建请求的管理器
    opener = request.build_opener(http_handler,https_handler,cookie_handler)

    # 打开登录页面后自动通过用户名密码登录
    # 获取登陆页面
    url = 'http://www.renren.com/PLogin.do'
    data = {
        'email':'18767101020',
        'password':'18767101020'
    }
    data =  parse.urlencode(data)
    res = request.Request(url=url,data=data.encode())
    # 使用opener发起请求
    res = opener.open(res)

    # 打印下cookie
    '''
    cookie的属性
    name: 名称
    value： 值
    domain：可以访问此cookie的域名
    path： 可以发昂文此cookie的页面路径
    expires：过期时间
    size： 大小
    Http字段
    '''

    # print(cookie)
    # for item in cookie:
    #     # print('item的类型是{0}'.format(type(item)))
    #     print('item的内容是{0}'.format(item))
    #     for i in dir(item):
    #         print('item中的类型{0}'.format(i))

    # 通过filecookie文件保存cookie
    # ignor_discard表示及时cookie将要被丢弃也要保存下来
    # ignore_expire表示如果该文件中cookie即使已经过期，保存
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 访问隐私页面需要的网址
    urlprive = 'http://www.renren.com/290945236/profile'
    # 自动提取反馈回来的cookie
    # 利用提取的cookie登录隐私页面
    res = opener.open(urlprive)
    htmlprive = res.read().decode()
    with open('rsp.html', 'w') as f:
        f.write(htmlprive)

def htmlcookietxt():
    cookie = cookiejar.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    cookie_handler = request.HTTPCookieProcessor(cookie)
    http_handler = request.HTTPHandler()
    https_handler = request.HTTPSHandler()
    opener = request.build_opener(http_handler, https_handler, cookie_handler)

    urlprive2 = 'http://www.renren.com/290945236/profile'
    res = opener.open(urlprive2)
    htmlprive2 = res.read().decode()
    with open('rsp2.html', 'w') as f:
        f.write(htmlprive2)




if __name__ == '__main__':
    # htmlfanyi(url='https://fanyi.baidu.com/sug', kw='girl')
    # kw = input("Input your keyword:")
    # htmlfinder(url='http://www.baidu.com/s?', wd=kw)
    # htmlproxy(url='http://www.baidu.com')
    # htmllogin_session()
    # htmllogin_cookie()
    # htmlcookietxt()


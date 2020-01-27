from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def appresponse(request):
    return HttpResponse('欢迎访问佳郡的网站！')


def appparam(request,year):
    print('进来2')
    return  HttpResponse('这里可以显示的年份{0}'.format(year))

def myview(r):
    # 让界面返回404，Http404为Exception子类,所以需要raise使用
    raise Http404
    return  HttpResponse('这是一个我们自己创建的视图')

def app_suburl(r):
    print(r)
    return HttpResponse('这是一个在myapp中处理的url')

def index_1(r,page,pn):
    return HttpResponse('index_1返回')

def index_2(r,page_number):
    return HttpResponse('index_2返回页数是：{0}'.format(page_number))

def extrem(r,name):
    return HttpResponse('额外的参数返回：{0}'.format(name))

# 访问的名字反相解析
def revparse(r):
    return HttpResponse('这个url有一个名字：{0}'.format(reverse('newfanjj')))

# 重定向
def index_3(r):
    return HttpResponseRedirect(reverse('newfanjj'))

'''
HttpResponse详解
方法
init ：使用页内容实例化HttpResponse对象
write(content)：以文件的方式写
flush()：以文件的方式输出缓存区
set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
key,value都是字符串类型
max_age是一个整数，表示在指定秒数后过期
expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
max_age与expires二选一
如果不指定过期时间，则两个星期后过期
delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生

'''
# 将url中的参数和对应的值一一返回，用，间隔
def mygetvalue(r):
    rst =''
    for k,v in r.GET.items():
        rst+=k + '---->'+v
        rst+=','
    return HttpResponse('得到的url中的参数值为：{0}'.format(rst))

# 使用模块需要先将模板路径放进setting,使用render函数来展示页面模板
def mygetvalue1(r):
    # 环境变量
    # c =dict()
    return render(r,template_name='fanjj_post.html')

# 如果遇到：CSRF verification failed. Request aborted.，在setting中的中间件csrf防护关闭
# render使用

def mypostvalue(r):
    rst =''
    for k,v in r.POST.items():
        rst+=k + '--->'+v
        rst+=','
    return HttpResponse('得到的页面返回值有：{0}'.format(rst))

# 这个是使用模板 + 自已输入的参数组成
def rendertest1(r):
    # 环境变量参数
    c = dict()
    c['name'] = 'kareen'
    rsp = render(r,template_name='rendertest.html',context=c)
    return rsp


# 先得到模板，再进行返回
def rendertest2(r):
    from django.template import loader
    # 得到模板
    t = loader.get_template('rendertest.html')
    r = t.render({'name':'kareen2'})
    return HttpResponse(r)

def get404(r):
    from django.views import defaults
    return defaults.page_not_found(r,exception='404.html')
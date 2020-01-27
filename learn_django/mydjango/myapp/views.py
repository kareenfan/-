from django.shortcuts import render
from django.http import HttpResponse,Http404
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

def revparse(r):
    return HttpResponse('这个url有一个名字：{0}'.format(reverse('newfanjj')))

"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
# 导入app中的视图views
from myapp import views as myview
from myapp import myapp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #地址匹配，尖号(^)和美元符号($)，^表示从头开始匹配   $表示以xxx结尾
    # 正常映射，视图函数中只有名称，无括号和参数
    path(r'kareen/',myview.appresponse),

    # 使用正则表达式的要使用re_path，
    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问好加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号表示出现的次数，此处4表示只能出现四个0-9的数字
    re_path(r'^kareener/(?P<year>[0-9]{4})/',myview.appparam),

#     url在app中处理
# 如果所有应用URL都集中tulingxueyuan/urls.py中,可能导致文件的臃肿,可以把urls具体功能逐渐分散到每个app中
# 使用方法
# 确保include被导入
# 写主路由的开头url
# 写子路由
# 编写views函数
# 同样可以使用参数
    path(r'myapp/',include(myapp_urls)),
#     url中嵌套参数,index_1是bad,需要三个入参，index2是good，?:明忽略此参数
    re_path(r'index_1/(page-(\d+)/)?$',myview.index_1),
    re_path(r'index_2/(?:page-(?P<page_number>\d+)/)?$',myview.index_2),
    # 传递额外参数，该值不在url中，但是会传到后面,参数不仅仅来自以URL,还可能是我们自己定义的内容
    path(r'extrem/',myview.extrem,{'name':'fanjj'}),

    # 反相解析
    path(r'youna/',myview.revparse,name='newfanjj'),
#     创建视图
    path(r'myviews/',myview.myview),
#     重定向，服务器跳转
    path(r'index_3/',myview.index_3),
#     GET属性练习
#     http://127.0.0.1:8000/index_get/?name=kareen&age=28
#     可以在问号后面跟参数访问
    path(r'index_get/',myview.mygetvalue),
#     POST属性练习，从表单页面提交后，在下一个页面获取
    path(r'index_get1/',myview.mygetvalue1),
    path(r'index_post/',myview.mypostvalue),
# 使用模板返回练习
    path(r'rendertest1/',myview.rendertest1),
    path(r'rendertest2/', myview.rendertest2),
#     系统内置视图，可直接使用，例如404报错
    path(r'get404/',myview.get404),

]
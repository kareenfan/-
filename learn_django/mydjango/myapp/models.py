from django.db import models

# Create your models here.
'''
定义和数据库表映射的类

在应用中的models.py文件中定义class
所有需要使用ORM的class都必须是 models.Model 的子类
class中的所有属性对应表格中的字段
字段的类型都必须使用 modles.xxx 不能使用python中的类型
字段常用参数

max_length : 规定数值的最大长度
blank : 是否允许字段为空,默认不允许
null : 在DB中控制是否保存为null, 默认为false
default : 默认值
unique : 唯一
verbose_name : 假名

'''
class myapp(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=200)

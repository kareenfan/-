import paramiko
import re

# 实例化一个transport对象
transport = paramiko.Transport(('192.168.47.236',22))
# 建立连接
transport.connect(username='pythonTest',password='qweqwe')
# 建立ssh对象
ssh = paramiko.SSHClient()
# 绑定transport到ssh对象
ssh._transport=transport
# 执行命令
stdin,stdout,stderr=ssh.exec_command('ls')
# 打印输出
ff =stdout.read().decode()
#print(a)
#print(type(a))
print('_________________________________________________')
# 匹配caifu_custquery.log.日期格式
a = re.finditer('caifu_custquery\.log\.\d{8}',ff)

# 匹配caifu_log.日期格式

b = re.finditer('(caifu){0,1}_log\.\d{8}', ff)

# 匹配中文格式的log.日期格式
c = re.finditer('[新建文本文档]{6}\D{0,1}([(]{1}\d{1}[)]{1}){0,1}\D{1,11}([(]{1}\d[)]{1}\D){0,1}\d{8}', ff)

for aa in a:

    print(aa.group())

for bb in b:
    print(bb.group())

for cc in c:
    print(cc.group())
# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-03 10:12  
# software  :python_learn 

'''
MUA(MailUserAgent)邮件用户代理
MTA(MailTransferAgent)邮件传输代理
MDA(MailDeliveryAgent)邮件投递代理

发送流程：（发送方QQ邮箱，接受方新浪邮箱）
MUA->MTA, 邮件已经在服务器上了
qq MTA->.........->sina MTA, 邮件在新浪的服务器上
sina MTA-> sina MDA, 此时邮件已经在你的邮箱里了
sina MDA -> MUA(Foxmail/Outlook), 邮件下载到本地电脑

发送： MUA->MTA with SMTP:SimpleMailTransferProtocal，包含MTA->MTA
接受： MDA->MUA with POP3 and IMAP：PostOfficeProtocal v3 and InternetMessageAccessProtocal v4
发邮件前需要得到邮箱的授权码
注册邮箱（以qq邮箱为例）
第三方邮箱需要特殊设置， 以qq邮箱为例
进入设置中心
取得授权码
'''
import smtplib
from email.mime.text import MIMEText #传输文本
from email.mime.multipart import MIMEBase,MIMEMultipart  #传输附件
from email.header import Header

# 发送邮件需要几个入参
def send_email(from_addr,from_pwd,to_addr,smtp_srv,msg):
    try:
        # 两个参数
        # 第一个是服务器地址，但一定是bytes格式，所以需要编码encode
        # 第二个参数是服务器的接受访问端口,465默认的访问安全端口
        srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)   # SMTP协议默认端口25
        # 登录邮箱发送
        srv.login(from_addr, from_pwd)
        # 发送邮件
        # 三个参数
        # 1. 发送地址
        # 2. 接受地址，必须是list形式
        # 3. 发送内容，作为字符串发送
        srv.sendmail(from_addr, [to_addr], msg.as_string())
        print('邮件发送成功')
        srv.quit()
    except Exception as e:
        print(e)

# 发件人信息，密码为授权码
from_addr ='405838720@qq.com'
from_pwd = 'huhtydjzrcobbjfc'
# 收件人信息
to_addr = '18767101020@163.com'
# 发件人邮箱的SMTP服务器地址
smtp_srv = 'smtp.qq.com'

# 发送内容
# MIMEText三个主要参数
# 1. 邮件内容
# 2. MIME子类型，在此案例我们用plain表示text类型,html表示html类型
# 3. 邮件编码格式

# 发送邮件,发送纯文本邮件
msg = MIMEText("hello I am kareen this message is html" ,'plain','utf-8')
# send_email(from_addr,from_pwd,to_addr,smtp_srv,msg)

# 发送邮件，有html格式
mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1> 这是一封HTML格式邮件</h1>
        </body>
        </html>
        """
htmlmsg = MIMEText(mail_content,'html', 'utf-8')
send_email(from_addr,from_pwd,to_addr,smtp_srv,htmlmsg)

# 带附件的内容发送
mail_mul = MIMEMultipart()
msg = MIMEText(mail_content,'html', 'utf-8')
mail_mul.attach(msg)

# 增加附件内容
with open('ORM.py', 'rb') as f:
    s = f.read()
    m = MIMEText(s, 'base64','utf-8')
    m['Content-Tpye']= 'application/octet-stream'
    m["Content-Disposition"] = "attachment; filename='ORM.py'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)
# 发送带内容和附件
send_email(from_addr,from_pwd,to_addr,smtp_srv,mail_mul)

# 增加主题
msg = MIMEText("hello I am kareen this message is html", 'plain','utf-8')
header_sub = Header('python发送消息', 'utf-8')
msg['Subject'] = header_sub

send_email(from_addr,from_pwd,to_addr,smtp_srv,msg)

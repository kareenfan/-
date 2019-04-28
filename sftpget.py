#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:钱可文
# datetime:2019-04-28 17:57
# software: PyCharm
import paramiko
import traceback
import re
from pythontest.src.writelog import *
from pythontest.src.getconfig import *
from pythontest.src.sendmessage import *


def ShhClient():  # SftpIpAderess, SftpPort, SftpUserName, SftpPassWord,SftpCommand

    SftpIpAderess = getConfigValue("sftp", "IPADRESS")
    SftpPort = 22
    SftpUserName = getConfigValue("sftp", "USERNAME")
    SftpPassWord = getConfigValue("sftp", "PASSWD")
    SftpCommand = 'ls'

    try:
        # 创建ssh对象
        ssh = paramiko.SSHClient()
        print(SftpIpAderess)
        # 添加允许新人列表
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 创建ssh连接，IpAderess IP地址, Port 端口, UserName 用户名, PassWord 密码
        ssh.connect(hostname=SftpIpAderess, port=SftpPort, username=SftpUserName, password=SftpPassWord)

        strin, strout, strerr = ssh.exec_command(SftpCommand)
        Commandresult = strout.read()
        print(str(Commandresult, 'utf-8'))
        return Commandresult
    except Exception  as err:
        traceback.print_exc()
    finally:
        ssh.close()


def SftpPutGet():
    SftpIpAderess = getConfigValue("SFTP", "IPADRESS")
    SftpPort = 22
    SftpUserName = getConfigValue("SFTP", "USERNAME")
    SftpPassWord = getConfigValue("SFTP", "PASSWD")
    messagge = ""
    try:
        transport = paramiko.Transport((SftpIpAderess, SftpPort))
        transport.connect(username=SftpUserName, password=SftpPassWord)
        # 实例化对象
        sftp = paramiko.SFTPClient.from_transport(transport)
        WriteLevlog("info","开始扫描sftp文件！")
        result1 = sftp.listdir()
        WriteLevlog("info","结束扫描sftp文件，开始匹配文件名！")
        for name in result1:  # 从list中取出文件名
            pattern = re.compile(r'\d{6,}')
            result2 = pattern.findall(name)  # 匹配文件名中存在6位数字的文件名
            if result2:
                for lastname in result2:  # 从list中取出6位数字
                    if lastname > '20170717':  # 下载日期大于20170707的文件
                        sftp.get(remotepath=name, localpath="../test/" + name)  # 开始下载
                        messagge = messagge + "\n" + name
        WriteLevlog("info", "以下文件："+messagge + " 下载成功")
        #发送钉钉消息
        #SendMess(messagge + "-下载成功！")
    except Exception as error:
        WriteLevlog("error", error)
    finally:
        # 关闭链接
        sftp.close()



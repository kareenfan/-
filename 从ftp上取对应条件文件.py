import paramiko
import re
import os

targethost = "192.168.47.236"
targetport = 22
timeout = 30
sshuser = "pythonTest"
sshpassword = "qweqwe"

# 登陆sftp并执行相应的命令
def sftp_command(command):
    try:
        # 实例化一个连接
        transport = paramiko.Transport(targethost,targetport)
        # 建立链接
        transport.connect(username=sshuser,password=sshpassword)
        # 建立ssh对象
        ssh = paramiko.SSHClient()
        # 绑定transport到ssh对象
        ssh._transport=transport
        # 执行命令
        stdin,stdout,stderr= ssh.exec_command(command)
        # 打印输出
        ff = stdout.read().decode()
        print(ff)
    except Exception as e:
        print("error啦",e)
    finally:
        ssh.close()


def sftp_down_file(begindate,enddate):
    try:
        transport = paramiko.Transport(targethost,targetport)
        transport.connect(username=sshuser,password=sshpassword)
        # sftp链接
        ssh = paramiko.SFTPClient.from_transport(transport)
        aalist = ssh.listdir()
        print(aalist)
        #print(type(aalist))
        # 编译含有8位数字的文件
        paconbile = re.compile(r'\d{8,}')

        for remotefile in aalist:
            bblist = paconbile.findall(remotefile)
            #print("kan",bblist,bb)
            for cclist in bblist:
                if (cclist > begindate and cclist < enddate):
                    print(remotefile)
                    # 路径拼接
                    localfile = os.path.join('/Users/kareen/Documents/tmp/',remotefile)
                    print(localfile)
                    ssh.get(remotepath=remotefile, localpath=localfile)

    except Exception as e:
        print("报错啦",e)
    finally:
        ssh.close()

import ftplib
import socket

def ftp_login_download():
    # ftp登陆

    HOST = "ftp.acc.umu.se"
    DIR = 'Public/EFLIB/'
    FILE = 'README'
    # 1. 客户端链接远程主机上的FTP服务器

    try:
        f = ftplib.FTP()
        # 设置调试级别方便调试
        f.set_debuglevel(2)
        # 链接对应的主机
        f.connect(HOST)
    except Exception as e:
        print(e)
        exit()
    finally:
        print("connectted to host {0} ".format(HOST))

    # 2. 客户端输入用户名和密码（或者“anonymous”和电子邮件地址）
    try:
        # 登录如果没有输入用户信息，则默认使用匿名登录
        f.login()
    except Exception as e:
        print(e)
        exit()
    finally:

        print('Logged in as "anonymous"')

    # 3. 客户端和服务器进行各种文件传输和信息查询操作
    try:

        # 更改当前目录到指定目录
        f.cwd(DIR)
    except Exception as e:
        print(e)
        exit()
    finally:
        print('changed dir {0}'.format(DIR))

    try:
        # 从FTP服务器上下载文件
        # 第一个参数是ftp命令
        # 第二个参数是回调函数
        # 此函数的意思是，执行RETR命令，下载文件到本地后，运行回调函数
        f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
    except Exception as e:
        print(e)
        exit()

    # 4. 客户端从远程FTP服务器退出，结束传输
    f.quit()


if __name__ == '__main__':
    # sftp_command('ls -l')
    sftp_down_file('20170102','20180101')
    # ftp_login_download()

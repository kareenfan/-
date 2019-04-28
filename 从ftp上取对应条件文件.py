import paramiko
import re

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


def sftp_down_file():
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

        for bb in aalist:
            bblist = paconbile.findall(bb)
            #print("kan",bblist,bb)
            for cclist in bblist:
                if cclist > '20170711':
                    print(bb)



    except Exception as e:
        print("报错啦",e)
    finally:
        ssh.close()

if __name__ == '__main__':
    #sftp_command('ls -l')
    sftp_down_file()

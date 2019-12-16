# @Time     :2019/11/26 11:30
# @Author   :dengyuting
# @File     :time_func.py
import paramiko

ssh_config = {
        'hostname': '115.29.205.99',
        'port': '62222',
        'username': 'root',
        'password': '#rDCAzPop&De5E%ozL!lsnWptIG9k&ea'
}


def set_time(time1):
    ssh = paramiko.SSHClient()  # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(**ssh_config)
#   cmd = f'date -s "{time1}";hwclock -w'
    stdin, stdout, stderr = ssh.exec_command(cmd) #执行命令
    result = stdout.read() or stderr.read()
    ssh.close()
    print("当前时间", result.decode())
def Recovery_time(time1):
    ssh = paramiko.SSHClient()  # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(**ssh_config)

    stdin, stdout, stderr = ssh.exec_command(time1) #执行命令
    result = stdout.read() or stderr.read()
    ssh.close()
    print(" 当前时间 ", result.decode())
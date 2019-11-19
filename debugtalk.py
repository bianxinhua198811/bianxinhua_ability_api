import csv
import hashlib
import json
import random
import time
import uuid
import paramiko


import pymysql


def sleep(n_secs):
    time.sleep(n_secs)

# def get_base_url(env_type="test"):
#     """
#     根据配置选择运行环境
#     :param env_type:
#     :return:
#     """
#     if env_type == "test":
#         return "https://ability-test.fjmaimaimai.com"
#     else:
#         return "https://ability-prod.fjmaimaimai.com"

def get_nowtime():
    return time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))

def make_time():
    """
    生成当前时间戳
    """
    return str(round(time.time() * 1000))

def make_uuid():
    """
    基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性
    """
    return str(uuid.uuid1())

def make_sign(currtime, uuid, accessstoken):
    """
    生成签名
    :param currtime:
    :param uuid:
    :param accessstoken:
    :return:
    """
    sign = 'v!(MmM' + currtime + uuid + accessstoken + 'MmM)i^'
    #sign = 'v!(MmM' + '1571277272600' + '10464980-f081-11e9-864d-e0d55e6d2c5c' +'4ixe5eiDmeaimcXYR3EYw2W43yMbQR7e'+ 'MmM)i^'
    sign = hashlib.sha256(sign.encode("utf-8"))
    encrypts = sign.hexdigest()
    return encrypts

def teardown_hook_get_accesstoken(response):
    if response.status_code == 200:
        jsondata = json.loads(response.text)
        access_token =jsondata['data']['accessToken']
    try:
        # 保存token到文件
        with open('config/accessToken.csv','w') as f:
            f.write(access_token)
            print('写入成功，access_token：{}'.format(access_token))
            f.close()
    except Exception as e:
        print('写入失败', e)
    return access_token

def teardown_hook_get_authcode(response):
    if response.status_code == 200:
        jsondata = json.loads(response.text)
        auth_code =jsondata['data']['authCode']
    try:
        # 保存token到文件
        with open('config/authCode.csv','w') as f:
            f.write(auth_code)
            print('写入成功，authCode：{}'.format(auth_code))
            f.close()
    except Exception as e:
        print('写入失败', e)
    return auth_code

def get_accesstoken():
    try:
        with open('config/accessToken.csv','r') as f:
            accseetoken_value = f.read()
            print('读取accseetoken_value成功：{}'.format(accseetoken_value))
            f.close()
    except Exception as e:
        print('读取失败', e)
    accseetoken_value = str(accseetoken_value)
    return accseetoken_value

def get_authcode():
    try:
        with open('config/authCode.csv','r') as f:
            authcode_value = f.read()
            print('读取authcode_value成功：{}'.format(authcode_value))
            f.close()
    except Exception as e:
        print('读取失败', e)
    authcode_value = str(authcode_value)
    return authcode_value

def setup_hook_clean_db():
    """
    初始化时清理数据库中的历史数据
    :return:
    """
    db = pymysql.connect(host="115.29.205.99",port=3306,user="shiqiurong", password="QGaBlwXT123dfvc7ip",db= "ability_display",charset='utf8')
    cursor = db.cursor()
    try:
        #删除评论
        cursor.execute("delete d from comment d LEFT JOIN  comment a on d.id=a.cid LEFT JOIN question b on a.id = b.id LEFT JOIN departments c on  b.relevantDepartmentId =c.id where   c.company_id =42 and c.enabled = 1")
        cursor.execute("delete d from comment d LEFT JOIN solution a on d.id=a.id LEFT JOIN question b on a.qid = b.id LEFT JOIN departments c on  b.relevantDepartmentId =c.id where   c.company_id =42 and c.enabled = 1")
        cursor.execute("delete d from comment d LEFT JOIN question a on d.id =a.id  LEFT JOIN departments b on  a.relevantDepartmentId =b.id  where b.company_id =42 and b.enabled = 1")
        #删除解决方案
        cursor.execute("delete a from solution a LEFT JOIN question b on a.qid=b.id LEFT JOIN departments c  on b.relevantDepartmentId=c.id where c.company_id =42 and c.enabled = 1")
        #删除问题
        cursor.execute("delete a from question a LEFT JOIN departments b on a.relevantDepartmentId=b.id where b.company_id =42 and b.enabled = 1")
        #删除用户消息表
        cursor.execute("delete a from user_msg a LEFT JOIN user_info b on a.uid=b.uid   where b.company_id=42")
        # 删除用户星数变动表
        cursor.execute("delete a from user_score_change a LEFT JOIN user_info b on a.uid=b.uid   where b.company_id=42")
        # 删除用户解决申请表
        cursor.execute("delete from user_question_solve where uid in (select uid from user_info where company_id=42)")
        # 删除质疑表
        cursor.execute("delete from doubt where company_id=42")
        # 删除额外加分表
        cursor.execute("delete from bonus_point where company_id=42")
        # 删除公告表
        cursor.execute("delete from bulletin where company_id=42")
        # 删除表彰管理表
        cursor.execute("delete from commend where company_id=42")
        # 删除用户消息表
        cursor.execute("delete from user_msg where uid in (select uid from user_info where company_id=42)")
        # 删除用户同感表
        cursor.execute("delete from user_sympathy where uid in (select uid from user_info where company_id=42)")
        # 删除问题标记表
        cursor.execute("delete from question_marks where uid in (select uid from user_info where company_id=42)")
        # 删除问题标记结果表
        cursor.execute("delete from question_marks_result where uid in (select uid from user_info where company_id=42)")
        # 删除用户提交表
        cursor.execute("delete from user_commit where uid in (select uid from user_info where company_id=42)")
        # 删除问题提交表
        cursor.execute("delete a from question_commit a LEFT JOIN user_commit b on a.commitId =b.id LEFT JOIN user_info c on b.uid =c.uid where c.company_id =42")
        db.commit()
        print("delete OK")
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()


def add(x, y) -> int:
    """
    对两个数相加
    :param x:
    :param y:
    :return:
    """
    return int(int(x)+y)

def pagesize(x, y) -> int:
    """
    判断页数
    :param x:
    :param y:
    :return:
    """
    rem = (int(int(x)%y))
    if rem == 0 :
        page_size = int(int(x)/y-1)
    else:
        page_size = int(int(x)/y)
    return page_size

def cal(x, y, z) -> int:
    return int(x-y*z)

def callen(value) -> int:
    return len(value)

def get_solveid(qid):
    #根据问题id，查询相应的解决申请表id
    db = pymysql.connect(host="115.29.205.99", port=3306, user="shiqiurong", password="QGaBlwXT123dfvc7ip",
                         db="ability_display", charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute('select id from user_question_solve where qid = %s',qid)
        result = cursor.fetchone()
        id = result[0]
        return id
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()


def isnull(response):
    jsondata= json.loads(response.content)
    if len(jsondata['data']['lists']) == 0:
        return 0
    else :
        return jsondata['data']['lists'][0]['id']
#以下与前面为同一方法
# def isnull(content):
#     print(content)
#     if len(content['lists']) == 0:
#         return 0
#     else :
#         return content['lists'][0]['id']


def qGrade(data):
    """
       判断是否有qGrade=0的问题
       :param x:
       :param y:
       :return:
   """
    xlen = len(data['lists'])
    i = 0
    count = 0
    for i in range(xlen):
        if data['lists'][i]['qGrade'] == 0:
            count=count + 1
        i = i+1
    if count == 0:
        return 1
    else:
        return 0


def len_list(response):
    # 计算返回的列表数组长度
    xlen = 0
    jsondata = json.loads(response.content)
    xlen = len(jsondata['data']['lists'])
    return xlen


def set_time(time1):
    ssh = paramiko.SSHClient()  # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='115.29.205.99', port='62222', username='root', password='#rDCAzPop&De5E%ozL!lsnWptIG9k&ea')
    cmd = f'date -s "{time1}";hwclock -w'
    stdin, stdout, stderr = ssh.exec_command(cmd) #执行命令
    result = stdout.read() or stderr.read()
    ssh.close()
    print("当前时间", result.decode())
def Recovery_time(time1):
    ssh = paramiko.SSHClient()  # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='115.29.205.99', port='62222', username='root', password='#rDCAzPop&De5E%ozL!lsnWptIG9k&ea')

    stdin, stdout, stderr = ssh.exec_command(time1) #执行命令
    result = stdout.read() or stderr.read()
    ssh.close()
    print(" 当前时间 ", result.decode())
# set_time('2019-08-28 23:19:40')

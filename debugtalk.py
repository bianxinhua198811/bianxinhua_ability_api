import csv
import hashlib
import json
import random
import time
import uuid

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

def teardown_hook_clean_db():
    """
    结束时清理数据库中的所有数据
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
        db.commit()
        print("delete OK")
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()

def add(x, y) -> str:
    """
    对两个数相加
    :param x:
    :param y:
    :return:
    """
    return str(int(x)+y)


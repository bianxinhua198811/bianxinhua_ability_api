import json
import time
from helpfunc.db_func import *
from helpfunc.header_func import *
from helpfunc.login_func import *
from helpfunc.time_func import *


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


# def isnull(response):
#     jsondata= json.loads(response.content)
#     if len(jsondata['data']['lists']) == 0:
#         return 0
#     else :
#         return jsondata['data']['lists'][0]['id']
#以下与前面为同一方法
def isnull(content):
    print(content)
    if len(content['lists']) == 0:
        return 0
    else :
        return content['lists'][0]['id']


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


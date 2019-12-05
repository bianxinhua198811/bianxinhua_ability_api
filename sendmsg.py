# @Time     :2019/12/4 9:37
# @Author   :dengyuting
# @File     :sendmsg.py
import json

import requests
import os

JENKINS_URL = str(os.getenv("JENKINS_URL"))
BUILD_NUMBER = str(os.getenv("BUILD_NUMBER"))
JOB_NAME = str(os.getenv("JOB_NAME"))
CAUSE = str(os.getenv("CAUSE"))
BUILD_URL = str(os.getenv("BUILD_URL"))
BUILD_USER = str(os.getenv("BUILD_USER"))

path = os.path.dirname(__file__)
summary_file = os.path.join(path, 'logs', 'ability_suites.summary.json')

def getresult():
    try:
        with open(summary_file, 'rb') as f:
            f = f.read()
            jsonfile = json.loads(f)
            if jsonfile["success"] == True:
                result = "SUCCESS"
                total = jsonfile["stat"]["testcases"]["total"]
                success = jsonfile["stat"]["testcases"]["success"]
                fail = jsonfile["stat"]["testcases"]["fail"]
                return result, total, success, fail
    except Exception as err:
        print("this is err:{}" .format(err))

def sendinfo():
    r =getresult()
    data = {}
    data['msgtype'] = 'text'
    data['text'] = {}
    data['text']['content'] = '【ability接口自动化测试-测试环境】 \n 构建人：' +BUILD_USER+ \
                              '\n 测试执行结果：'+r[0]+ '\n TOTAL：' +str(r[1]) +'\n SUCCESS:' +str(r[2])+ '\n FAIL:' +str(r[3])+ \
                              '\n 查看控制台：' +BUILD_URL+'console \n 测试报告地址：XXXXXXXX \n'
    # data['text']['mentioned_mobile_list'] = ["13559112969","@all"]

    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b8028a75-89ff-4dc4-a1a7-6d8e3fd44552'
    headers = {'Content-Type': 'application/json'}

    requests.post(url, json=data, headers=headers)

if __name__ == '__main__':
    sendinfo()



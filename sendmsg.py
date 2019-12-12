# @Time     :2019/12/4 9:37
# @Author   :dengyuting
# @File     :sendmsg.py
import json

import requests
import os

"""
jenkins通知测试执行结果
"""

JENKINS_URL = str(os.getenv("JENKINS_URL"))
BUILD_NUMBER = str(os.getenv("BUILD_NUMBER"))
JOB_NAME = str(os.getenv("JOB_NAME"))
CAUSE = str(os.getenv("CAUSE"))
BUILD_URL = str(os.getenv("BUILD_URL"))
JOB_URL = str(os.getenv("JOB_URL"))

path = os.path.dirname(__file__)
summary_file = os.path.join(path, 'logs', 'ability_suites.summary.json')

def getresult():
    try:
        with open(summary_file, 'rb') as f:
            f = f.read()
            jsonfile = json.loads(f)
            if jsonfile["success"] == True:
                result = "SUCCESS"
            else:
                result = "FAIL"
            total = jsonfile["stat"]["testcases"]["total"]
            success = jsonfile["stat"]["testcases"]["success"]
            fail = jsonfile["stat"]["testcases"]["fail"]
            duration = round(jsonfile["time"]["duration"])
            # teststeps_total = jsonfile["stat"]["teststeps"]["total"]
            # teststeps_successes = jsonfile["stat"]["teststeps"]["successes"]
            # teststeps_failures = jsonfile["stat"]["teststeps"]["failures"]
            # teststeps_errors = jsonfile["stat"]["teststeps"]["errors"]
            # teststeps_skipped = jsonfile["stat"]["teststeps"]["skipped"]
            return result, total, success, fail, duration
    except Exception as err:
        print("this is err:{}" .format(err))

def sendinfo():
    r =getresult()
    data = {}
    data['msgtype'] = 'text'
    data['text'] = {}
    data['text']['content'] = '【'+JOB_NAME+'】\n 测试执行结果：'+r[0]+ \
                              '\n 执行时间：' +str(r[4])+ \
                              's\n TOTAL：' +str(r[1]) +'\n SUCCESS：' +str(r[2])+ '\n FAIL：' +str(r[3])+ \
                              '\n 查看控制台：' +BUILD_URL+'console \n 测试报告地址：' +JOB_URL+'Ability_20Test_20Report/ \n'
    # data['text']['mentioned_mobile_list'] = ["13559112969","@all"]

    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b8028a75-89ff-4dc4-a1a7-6d8e3fd44552'
    headers = {'Content-Type': 'application/json'}

    requests.post(url, json=data, headers=headers)

if __name__ == '__main__':
    sendinfo()



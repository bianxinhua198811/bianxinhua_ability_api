# @Time     :2019/11/26 11:23
# @Author   :dengyuting
# @File     :login_wrap.py
import json


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

def teardown_hook_get_refreshtoken(response):
    if response.status_code == 200:
        jsondata = json.loads(response.text)
        refresh_token =jsondata['data']['refreshToken']
    try:
        # 保存token到文件
        with open('config/refreshToken.csv','w') as f:
            f.write(refresh_token)
            print('写入成功，refresh_token：{}'.format(refresh_token))
            f.close()
    except Exception as e:
        print('写入失败', e)
    return refresh_token

def teardown_hook_get_authcode(response):
    if response.status_code == 200:
        jsondata = json.loads(response.text)
        auth_code = jsondata['data']['authCode']
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

def get_refreshtoken():
    try:
        with open('config/refreshToken.csv','r') as f:
            refreshtoken_value = f.read()
            print('读取refreshtoken_value成功：{}'.format(refreshtoken_value))
            f.close()
    except Exception as e:
        print('读取失败', e)
    refreshtoken_value = str(refreshtoken_value)
    return refreshtoken_value

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
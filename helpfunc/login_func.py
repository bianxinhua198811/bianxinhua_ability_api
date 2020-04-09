#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2020/4/9 11:36
# @Author:bxh
# @file: login_func.py
import  json

def teardown_hook_get_authcode(response):

    if response.status_code ==200:

        jsondata = json.loads(response.text)

        auth_code = jsondata['data']['authCode']

    try:
        # 保存token到文件
        with open("E:/mmm-auto/ability_api/config/authCode.csv", 'w+') as f:

            f.write(auth_code)

            print('写入成功，authCode：{}'.format(auth_code))

    except Exception as e:

        print('写入失败', e)

    return auth_code
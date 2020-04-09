#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2020/4/9 11:23
# @Author:bxh
# @file: header_func.py
import hashlib
import time
import uuid

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
    sign = hashlib.sha256(sign.encode("utf-8"))
    encrypts = sign.hexdigest()
    return encrypts
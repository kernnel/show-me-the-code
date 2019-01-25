#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: redis.py 
@time: 2019/01/25 15:31
@contact: 282458466@qq.com
"""
import random
import string

import redis


# count 数量
# length 长度
def code(count, length):
    # 生成激活码可能包含的字符集（大写字母、小写字母、数字）
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits

    return [''.join(random.sample(base, length)) for i in range(count)]


def save_code():
    r = redis.Redis(host='127.0.0.1', port=6379, db=15)
    rp = r.pipeline()
    for item in code(200, 15):
        rp.sadd('code', item)
    rp.execute()
    return r.scard('code')


save_code()

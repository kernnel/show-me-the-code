#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: code.py 
@time: 2019/01/25 14:32
@contact: 282458466@qq.com
"""
import random
import string


# count 数量
# length 长度
def code(count, length):
    # 生成激活码可能包含的字符集（大写字母、小写字母、数字）
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # arr = []
    # for i in range(count):
    #    print( ''.join(random.sample(base, length)))

    return [''.join(random.sample(base, length)) for i in range(count)]


print(code(200, 12))

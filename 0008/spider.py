#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: spider.py 
@time: 2019/01/28 10:19
@contact: 282458466@qq.com
"""

import requests


def baidu():
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url = "http://www.yingtaoyun.com/"
    r = requests.get(url, header)
    text = r.text

    print(text)


baidu()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author:kernnel
@file: url.py
@time: 2019/01/28 11:57
@contact: 282458466@qq.com
"""
import re

import requests


def yingtaoyun():
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url = "http://www.yingtaoyun.com/"
    r = requests.get(url, header)
    text = r.text
    urls = []
    url = re.compile(r'([https]+://[^\s]*)"')
    urls += url.findall(text)
    print(urls)


yingtaoyun()

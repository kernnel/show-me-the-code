#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: filter.py 
@time: 2019/01/29 16:37
@contact: 282458466@qq.com
"""

import re


def filter_word(word):
    txt = open("./filtered_words.txt", 'r').read()

    w = re.sub('|'.join(txt), "*", word)
    print(w)


word = "北京是个好城市,公务员比程序员还牛逼"
filter_word(word)

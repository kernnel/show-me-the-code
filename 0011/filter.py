#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: filter.py 
@time: 2019/01/29 16:29
@contact: 282458466@qq.com
"""
import re


def filter_word(word):
    txt = open("./filtered_words.txt", 'r').read()

    if len(re.findall(r'%s' % (word), txt)) == 0:
        print('Human Rights')  # 非敏感词时，则打印出 Human Rights !
    else:
        print('Freedom')  # 输入敏感词语打印出 Freedom !


word = "北京"
filter_word(word)


word2 = "上海"
filter_word(word2)

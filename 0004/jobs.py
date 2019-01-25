#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: jobs.py 
@time: 2019/01/25 16:55
@contact: 282458466@qq.com
"""

# 读取文件
import re


def statistical_word(file_name):
    # 获取文件
    txt = open(file_name, 'r').read().splitlines()

    # 文章行数
    lines_count = 0
    # 单词数
    words_count = 0
    # 字符数量
    chars_count = 0

    words_dict = {}
    lines_list = []

    # 逐行读取
    for line in txt:
        lines_count = lines_count + 1
        chars_count = chars_count + len(line)

        # 匹配单词
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            # 只要英文单词，删掉其他字符
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1

    return words_dict, lines_count, chars_count


file_name = "/Users/kernnel/pycharm/show-me-the-code/0004/jobs.txt"

(words_dict, lines_count, chars_count) = statistical_word(file_name)
print('words_count is', len(words_dict))

print('lines_count is', lines_count)

print('chars_count is', chars_count)

for k, v in words_dict.items():
    print(k, v)

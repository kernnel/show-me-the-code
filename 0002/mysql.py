#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: mysql.py 
@time: 2019/01/25 15:07
@contact: 282458466@qq.com
"""

'''
py_code 表
CREATE TABLE `py_code` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(255) DEFAULT '' COMMENT '激活码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''

import pymysql.cursors

import random
import string

host = 'localhost'
user = 'root'
pwd = '123456'
db = 'test'
charset = 'utf8mb4'


# count 数量
# length 长度
def code(count, length):
    # 生成激活码可能包含的字符集（大写字母、小写字母、数字）
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # arr = []
    # for i in range(count):
    #    print( ''.join(random.sample(base, length)))

    return [''.join(random.sample(base, length)) for i in range(count)]


# Connect to the database
connection = pymysql.connect(host=host,
                             user=user,
                             password=pwd,
                             db=db,
                             charset=charset,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record,batch insert
        sql = "INSERT INTO `py_code` (`code`) VALUES (%s)"
        cursor.executemany(sql, code(200, 15))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()

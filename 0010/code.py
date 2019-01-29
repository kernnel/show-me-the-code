#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
"""
@author:kernnel 
@file: code.py 
@time: 2019/01/29 14:55
@contact: 282458466@qq.com
"""

import random
import string

from PIL import Image, ImageDraw, ImageFont


# 随机输出四个字母:
def rndChar():
    # 第一种写法
    # str = ''
    # for i in range(4):
    #     # str += chr(random.randint(65, 90))
    #     str += random.choice(string.letters)

    # 第二种写法
    str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])
    return str


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


font = ImageFont.truetype('Arial.ttf', 66)
# 打开一个jpg图像文件，注意是当前路径:
width = 200
height = 80
im = Image.new('RGB', (width, height), rndColor2())
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 创建Draw对象:
draw = ImageDraw.Draw(im)
draw.text((0, 0), rndChar(), font=font, fill=rndColor2())
# 缩放到50%:
# im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('code.jpg', 'jpeg')

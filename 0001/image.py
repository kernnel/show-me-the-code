#!/usr/bin/env python3
# -*- coding:utf-8 _*-  
"""
@author:kernnel 
@file: image.py 
@time: 2019/01/24 17:44
@contact: 282458466@qq.com
"""
import random

from PIL import Image, ImageDraw, ImageFont


# 随机输出四个字母:
def rndChar():
    return chr(random.randint(65, 90)) * 4


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


font = ImageFont.truetype('Arial.ttf', 66)
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('04.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 创建Draw对象:
draw = ImageDraw.Draw(im)
draw.text((w / 2, 0), rndChar(), font=font, fill=rndColor2())
# 缩放到50%:
# 把缩放后的图像用jpeg格式保存:
im.save('new.jpg', 'jpeg')

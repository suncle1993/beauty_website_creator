#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 11/28/17 7:27 PM
@author: Chen Liang
@function: 去除右下角的澳门赌场广告水印，改成自己的水印
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image
import os


WATERMARK = Image.open('/tmp/private_watermark.jpg')
name_list = []


def add_watermarks(image_dir):
    for image in os.listdir(image_dir):
        if image[-3:] == 'jpg':
            print image
            add_watermark(image_dir, image)


def add_watermark(image_dir, image):
    global name_list
    try:
        img = Image.open('{}/{}'.format(image_dir, image))
        width, height = img.size
        rect = (width-160, height-35, width, height)
        img.paste(WATERMARK, rect)
        img.save('/tmp/photo/add_watermark/{}'.format(image))
    except Exception as e:
        print str(e)
        name_list.append(image)


if __name__ == '__main__':
    add_watermarks('/tmp/photo/haole_classified')
    print 'name_list: ', name_list

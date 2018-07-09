#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 11/28/17 6:50 PM
@author: Chen Liang
@function: 根据色情检测结果将图像分为清纯和性感两个分类，清纯图片改名为1__原名，性感图片改名为2__原名
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from porn_detector import PornDetector


def classify_photos(image_dir):
    for image in os.listdir(image_dir):
        if image[-3:] == 'jpg':
            if not (image.startswith('1__') or image.startswith('2__')):
                print image
                classify_photo(image_dir, image)


def classify_photo(image_dir, image):
    try:
        n = PornDetector('{}/{}'.format(image_dir, image))
        n.resize(max_height=1000, max_width=1000)
        n.parse()
        bool_value = n.judge()
        if bool_value is True:
            # 色情图像：即性感图像
            cmd = 'mv {image_dir}/{image} {image_dir}/2__{image}'.format(image_dir=image_dir, image=image)
            os.system(cmd)
        else:
            # 非色情图像：即清纯图像
            cmd = 'mv {image_dir}/{image} {image_dir}/1__{image}'.format(image_dir=image_dir, image=image)
            os.system(cmd)
    except Exception as e:
        print str(e)


if __name__ == '__main__':
    classify_photos('/tmp/photo/haole_no_porn')

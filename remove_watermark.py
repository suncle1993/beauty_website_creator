#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 11/24/17 8:08 PM
@author: Chen Liang
@function: 去除底部水印
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from PIL import Image
import os


def remove_watermark(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        region = image.crop((0, 0, width, height - 40))
        region.save('/tmp/test2/haole/{}'.format(os.path.basename(image_path)))
        return True
    except Exception as e:
        print str(e)
        return False


def remove_watermarks(image_dir):
    for image in os.listdir(image_dir):
        if image[-3:] == 'jpg':
            print image
            remove_watermark('{}/{}'.format(image_dir, image))


remove_watermarks('/tmp/test1/haole')

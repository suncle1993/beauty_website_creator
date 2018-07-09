#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 17-11-21 下午7:59
@author: Chen Liang
@function:  去除掉文件名中下标不符合的图像
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os
import re

pattern1 = '.*?【(\\d*)P】__(\\d*).jpg'
pattern2 = '.*?\((\\d*)P\)__(\\d*).jpg'
p1 = re.compile(pattern1)
p2 = re.compile(pattern2)


def remove(path):
    if os.path.exists(path):
        os.remove(path)


def photo_filter():
    n1 = 0
    n2 = 0
    for f in os.listdir('/tmp/photo/haole'):
        # print f
        n1 += 1
        is_remove = False
        m1 = p1.match(f)
        m2 = p2.match(f)
        try:
            if m1:
                total, index = m1.groups()
                if int(total) <= int(index):
                    is_remove = True
            elif m2:
                total, index = m2.groups()
                if int(total) <= int(index):
                    is_remove = True
            else:
                is_remove = True
        except Exception as e:
            print(str(e))
            is_remove = True
        if is_remove:
            print('remove: {}'.format(f))
            n2 += 1
            remove('/tmp/photo/haole/{}'.format(f))
    print n1, n2


if __name__ == '__main__':
    photo_filter()

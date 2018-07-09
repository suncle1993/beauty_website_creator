#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 11/24/17 8:53 PM
@author: Chen Liang
@function: 学习色情图片, 根据结果得出合适的ycbcr的cb范围和cr范围
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from porn_detector import PornDetector
import os
import pylab as pl

result = {'nude': [], 'sex': [], 'pure': []}


def learn(image_path):
    n = PornDetector(image_path)
    n.resize(max_height=1000, max_width=1000)
    n.parse()
    judge_value = (n.skin_region_nums, n.skin_pixel_num_rate, n.skin_region_area_rate)

    basename = os.path.basename(image_path)
    if basename.startswith('1'):
        result['nude'].append(judge_value)
    if basename.startswith('2'):
        result['sex'].append(judge_value)
    if basename.startswith('3'):
        result['pure'].append(judge_value)


def learn_photos(image_dir):
    for image in os.listdir(image_dir):
        if image[-3:] == 'jpg':
            print image
            learn('{}/{}'.format(image_dir, image))


def draw_skin_region_nums():
    nude = [res[0] for res in result['nude']]
    sex = [res[0] for res in result['sex']]
    pure = [res[0] for res in result['pure']]
    length = min([len(nude), len(sex), len(pure)])
    x = range(length)
    pl.plot(x, nude, 'r', label='nude')
    pl.plot(x, sex, 'g', label='sex')
    pl.plot(x, pure, 'y', label='pure')
    pl.xlabel('x axis')
    pl.ylabel('skin_region_nums axis')
    pl.grid(True)
    pl.legend(loc='upper left')
    pl.title('skin_region_nums')
    pl.show()


def draw_skin_pixel_num_rate():
    nude = [res[1] for res in result['nude']]
    sex = [res[1] for res in result['sex']]
    pure = [res[1] for res in result['pure']]
    length = min([len(nude), len(sex), len(pure)])
    x = range(length)
    pl.plot(x, nude, 'r', label='nude')
    pl.plot(x, sex, 'g', label='sex')
    pl.plot(x, pure, 'y', label='pure')
    pl.xlabel('x axis')
    pl.ylabel('skin_pixel_num_rate axis')
    pl.grid(True)
    pl.legend(loc='upper left')
    pl.title('skin_pixel_num_rate')
    pl.show()


def draw_skin_region_area_rate():
    nude = [res[2] for res in result['nude']]
    sex = [res[2] for res in result['sex']]
    pure = [res[2] for res in result['pure']]
    length = min([len(nude), len(sex), len(pure)])
    x = range(length)
    pl.plot(x, nude, 'r', label='nude')
    pl.plot(x, sex, 'g', label='sex')
    pl.plot(x, pure, 'y', label='pure')
    pl.xlabel('x axis')
    pl.ylabel('skin_region_area_rate axis')
    pl.grid(True)
    pl.legend(loc='upper left')
    pl.title('skin_region_area_rate')
    pl.show()


if __name__ == '__main__':
    learn_photos('/tmp/test1/Learn_photo')
    print result
    draw_skin_region_nums()
    draw_skin_pixel_num_rate()
    draw_skin_region_area_rate()

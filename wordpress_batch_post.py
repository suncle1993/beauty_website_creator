#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 12/7/17 5:02 PM
@author: Chen Liang
@function:
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
import datetime
import os
import time
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

wp_clt = Client('http://138.68.1.61/xmlrpc.php', 'snowlight437@gmail.com', 'xxxxxx')


def new_post(dir_str, photo_name):
    # prepare metadata
    category = '未分类'
    if photo_name.startswith('1__'):
        category = '清纯'
    if photo_name.startswith('2__'):
        category = '性感'
    data = {
        'name': photo_name,
        'type': 'image/jpeg',  # mimetype
    }
    # read the binary file and let the XMLRPC library encode it into base64
    with open('{}/{}'.format(dir_str, photo_name), 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
    response = wp_clt.call(media.UploadFile(data))
    attachment_id = response['id']
    post = WordPressPost()
    post.title = photo_name[3:-4]
    post.content = ''
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.comment_status = 'open'  # 不开启评论则设置成closed
    post.terms_names = {
        'post_tag': ['haole', category],  # 文章所属标签，没有则自动创建
        'category': ['haole', category]  # 文章所属分类，没有则自动创建
    }
    post.thumbnail = attachment_id  # 缩略图的id
    post.id = wp_clt.call(posts.NewPost(post))


def new_posts(dir_str):
    for photo_name in os.listdir(dir_str):
        try:
            new_post(dir_str, photo_name)
        except Exception as e:
            print str(e)


def get_post():
    p = wp_clt.call(posts.GetPost(142))
    print type(p), p
    print p.comment_status


if __name__ == '__main__':
    new_posts(dir_str='/tmp/photo')
    # get_post()

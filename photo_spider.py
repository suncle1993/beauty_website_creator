#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 17-11-18 下午2:56
@author: Chen Liang
@function:  简易爬虫，用于爬取图片
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import re
import requests


def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
            return r.text
    except Exception as e:
        print(str(e))
    return ''


def parse_and_format(html_str):
    start = '<div class="center margintop border clear main"><div class="title">'
    start_pos = html_str.find(start) + len(start)
    rest_str = html_str[start_pos:]
    title = rest_str[:rest_str.find('</div>')]
    return title, rest_str


def get_img_links(rest_str):
    pattern = r'src="https://pic.kanlela.com/images/pic/(.*?).jpg">'  # 非贪婪匹配
    nums = re.findall(pattern=pattern, string=rest_str, flags=re.S)
    links = []
    for num in nums:
        links.append("https://pic.kanlela.com/images/pic/{}.jpg".format(num))
    return links


def save_img(link, name):
    print('link={}, name={}'.format(link, name))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }
    try:
        img_content = requests.get(link, headers=headers)
        with open(name, 'wb') as f:
            f.write(img_content.content)
    except Exception as e:
        print str(e)


def handle_single_html_page(url):
    print(url)
    html_str = get_html_content(url)
    title, rest_str = parse_and_format(html_str)
    # print title, rest_str
    links = get_img_links(rest_str)
    print(links)
    for i, link in enumerate(links):
        save_img(link=link, name='/tmp/photo/haole/{}__{}.jpg'.format(title, i))


def handle_haoleav_page(url):
    print(url)
    c = get_html_content(url)
    pattern = r'<a href="/html/(.*?).html" target="_blank">'
    nums = re.findall(pattern=pattern, string=c, flags=re.S)
    links = []
    for num in nums:
        links.append("http://se.haoa08.com/html/{}.html".format(num))
    return links


def handle_haoleav_cute():
    for page in range(213, 229):
        url = 'http://se.haoa08.com/listhtml/4-{}.html'.format(page)
        links = handle_haoleav_page(url)
        print('page={}, handle url={}, links={}'.format(page, url, links))
        for link in links:
            try:
                handle_single_html_page(link)
            except Exception as e:
                print(str(e))
                pass


if __name__ == '__main__':
    handle_haoleav_cute()
    # handle_single_html_page('http://se.haoa08.com/html/121047.html')

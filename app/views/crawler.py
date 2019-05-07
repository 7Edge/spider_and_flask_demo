#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: crawler
# Date: 5/6/2019
import requests
from bs4 import BeautifulSoup
from flask import Blueprint

from app import db

crawler_bp = Blueprint(name='crawler', import_name=__name__)


@crawler_bp.route('/spider_autohome/')
def spider():  # 将汽车之家的新闻的：标题，标题图地址，brief简介， 文章出处地，文章地址。
    response = requests.get(url='https://www.autohome.com.cn/news/')
    response.encoding = 'gbk'
    bs = BeautifulSoup(markup=response.text, features='html.parser')
    articles_list = bs.find(name='div', attrs={'id': 'auto-channel-lazyload-article'}).find_all(name='ul')

    for article_item in articles_list:
        for li in article_item.find_all(name='li'):
            a = li.find(name='a')
            print(a)

    return response.text


if __name__ == '__main__':
    pass

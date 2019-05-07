#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: crawler
# Date: 5/6/2019
import requests
from bs4 import BeautifulSoup
from flask import Blueprint

from app import db
from app.models import AutoHomeNews

crawler_bp = Blueprint(name='crawler', import_name=__name__)


@crawler_bp.route('/spider_autohome/')
def spider():  # 将汽车之家的新闻的：标题，标题图地址，brief简介， 文章出处地，文章地址。
    response = requests.get(url='https://www.autohome.com.cn/news/')
    response.encoding = 'gbk'
    bs = BeautifulSoup(markup=response.text, features='html.parser')
    # 读取网页中的数据
    ul_list = bs.find(name='div', attrs={'id': 'auto-channel-lazyload-article'}).find_all(name='ul')

    news = list()

    for ul in ul_list:
        li_list = ul.find_all(name='li')
        for li in li_list:
            try:
                new_url = 'http://' + li.find(name='a').attrs.get('href').rsplit('//', maxsplit=1)[1]
                print(new_url)
                img_url = 'http://' + li.find(name='img').get('src').rsplit('//', maxsplit=1)[1]
                print(img_url)
                title = li.find(name='h3').text
                brief = li.find(name='p').text

                # 进入文章详情，获取文章来源

                detail_response = requests.get(url=new_url)
                detail_response.encoding = 'gbk'
                article_detail = BeautifulSoup(markup=detail_response.text, features='html.parser')
                source_tag = article_detail.find(name='div',
                                                 attrs={'class': 'article-info'}
                                                 ).find(name='span',
                                                        attrs={'class': 'source'})
                source = source_tag.text

                # 构建文章对象
                article_obj = AutoHomeNews(title=title, brief=brief, img=img_url, source=source, new_url=new_url)
                news.append(article_obj)
            except AttributeError:
                continue

    db.session.add_all(news)
    db.session.commit()
    db.session.remove()

    return response.text


if __name__ == '__main__':
    pass

#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: models
# Date: 5/6/2019

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, UniqueConstraint
# from sqlalchemy.orm import relationship

from app import db


# 爬去autohome新闻表
class AutoHomeNews(db.Model):
    __tablename__ = 'autohome_news'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(128))
    brief = Column(Text(512))
    img = Column(String(255))
    source = Column(String(255))
    new_url = Column(String(255))


if __name__ == '__main__':
    pass

#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: settings
# Date: 5/6/2019


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/autohome_news?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 5  # 数据库连接池大小
    SQLALCHEMY_MAX_OVERFLOW = 0  # 超过连接池大小外最多创建的连接
    SQLALCHEMY_POOL_RECYCLE = -1  # 多久之后对线程池中的线程进行一次连接的回收（重置;-1不回收）


class DevConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


if __name__ == '__main__':
    pass

#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: normal
# Date: 5/6/2019
from flask import Blueprint, render_template, url_for

normal_bp = Blueprint(name='normal', import_name=__name__)


@normal_bp.route('/index/')
def index():
    return render_template(template_name_or_list='index.html')


if __name__ == '__main__':
    pass

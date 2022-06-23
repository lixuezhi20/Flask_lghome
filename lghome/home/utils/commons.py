#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-12 14:55
# @Author  : Kevin
# @File    : commons.py
# @Software: PyCharm
from werkzeug.routing import BaseConverter


# 正则转换器
class ReConverter(BaseConverter):

    def __init__(self, url_map, regex):
        super(ReConverter, self).__init__(url_map)
        self.regex = regex


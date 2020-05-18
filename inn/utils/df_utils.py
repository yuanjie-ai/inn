#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : inn.
# @File         : df_utils
# @Time         : 2020/5/18 4:42 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import re


def df_select_columns(pattern, columns):
    return [c for c in columns if re.search(pattern, c)]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : __init__.py
# @Time         : 2020/4/13 11:41 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : https://github.com/brennv/namedtupled

from .namedtupled import mapper, ignore, reducer
from .integrations import load_json, load_yaml, load_lists, load_env

map = mapper
reduce = reducer
json = load_json
yaml = load_yaml
zip = load_lists
env = load_env

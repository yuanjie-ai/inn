#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : __init__.py
# @Time         : 2019-10-21 13:00
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from .Dataset import Dataset


def load_iris(batch_size=128):
    from sklearn import datasets
    ds = Dataset(batch_size)
    X, y = datasets.load_iris(True)
    return ds.from_cache(X, y)

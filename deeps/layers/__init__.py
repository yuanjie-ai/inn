#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : __init__.py
# @Time         : 2019-09-10 15:22
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
from functools import partial
from collections import Iterable

from keras.layers import Dense


# last layer: 'softmax' or 'sigmoid'
def getDenseList(unitsList, activation=None):
    assert isinstance(unitsList, Iterable)
    dense = partial(Dense, activation=activation)
    return map(dense, unitsList)



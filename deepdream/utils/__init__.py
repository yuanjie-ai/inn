#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : __init__.py
# @Time         : 2019-09-10 14:48
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
import numpy as np
from .cprint import cprint
from .timer import timer


def noramlize(x):
    return x / np.linalg.norm(x, 2, axis=len(x.shape) > 1, keepdims=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : data_processor_utils
# @Time         : 2020/4/21 12:04 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import numpy as np

_norm = lambda x, ord=1: x / np.linalg.norm(x, ord, axis=len(x.shape) > 1, keepdims=True)


def l1(x):
    return _norm(x)


def l2(x):
    return _norm(x, 2)

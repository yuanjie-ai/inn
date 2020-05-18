#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : utils
# @Time         : 2020/4/13 6:49 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from enum import Enum


# from collections import namedtuple
# FeatType = namedtuple('FeatType', ['Cat', 'Num'])('Cat', 'Num')
class FeatureType(str, Enum):
    DenseFeature = "DenseFeature"
    SparseFeature = "SparseFeature"
    SequenceFeature = "SequenceFeature"




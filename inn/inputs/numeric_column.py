#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : numeric_column
# @Time         : 2020/4/13 4:52 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :

import tensorflow as tf


def get_feature_columns(numeric_cols: list, shape=(1,), normalizer_fn=None):
    feature_columns = []
    feature_layer_inputs = {}

    for feat in numeric_cols:
        feature_column = tf.feature_column.numeric_column(feat, shape, normalizer_fn=normalizer_fn)
        feature_columns.append(feature_column)
        feature_layer_inputs[feat] = tf.keras.Input(feature_column.shape, name=feat)
    return feature_columns, feature_layer_inputs

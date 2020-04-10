#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : DataLoader
# @Time         : 2019-10-21 13:01
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import tensorflow as tf

"""
https://www.cnblogs.com/gengyi/p/11107492.html
https://tensorflow.google.cn/guide/data?hl=zh_cn
https://cs230-stanford.github.io/tensorflow-input-data.html#shuffle-and-repeat

tf.data.Dataset.zip
"""


class DataGenerator(object):

    def __init__(self, data_type='train', batchsize=128):
        self.data_type = data_type
        self.batchsize = batchsize

    def from_numpy(self, tensors, buffer_size=10000, seed=666):
        dataset = tf.data.Dataset.from_tensor_slices(tensors).batch(self.batchsize)
        if self.data_type in ('train', 'valid'):
            dataset = dataset.shuffle(buffer_size, seed)

        return dataset

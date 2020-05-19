#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : inn.
# @File         : Prediction
# @Time         : 2020/5/19 6:14 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import tensorflow as tf


class Prediction(tf.keras.layers.Layer):

    def __init__(self, task='binary', num_class=None, name='Prediction', **kwargs):
        super().__init__(name=name, **kwargs)

        self.task = task
        self.num_class = num_class

        if task == 'multiclass':
            assert num_class is not None, "num_class must not be None"

        self.task2activation = {'binary': 'sigmoid', 'multiclass': 'softmax', 'regression': None}
        if task not in self.task2activation:
            raise ValueError("task must be binary, multiclass or regression")

    def build(self, input_shape):
        super().build(input_shape)

        self.fc = tf.keras.layers.Dense(
            1 if self.task != 'multiclass' else self.num_class,
            activation=self.task2activation.get(self.task)
        )

    def call(self, inputs, **kwargs):
        return self.fc(inputs)

    def compute_output_shape(self, input_shape):
        if self.task == "multiclass":
            return (None, self.num_class)
        else:
            return (None, 1)

    def get_config(self, ):
        base_config = super().get_config()
        config = {'task': self.task, 'num_class': self.num_class}
        return {**base_config, **config}

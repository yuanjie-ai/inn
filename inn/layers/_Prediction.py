#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : PredictionLayer
# @Time         : 2020/4/29 6:07 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import tensorflow as tf
from tensorflow.keras.initializers import Zeros


class Prediction(tf.keras.layers.Layer):

    def __init__(self, task='binary', use_bias=False, num_class=0, name='Prediction', **kwargs):
        """https://github.com/shenweichen/DeepCTR/issues/211

        :param task: ["binary", "multiclass", "regression"]
        :param use_bias:
        :param kwargs:
        """
        super().__init__(name=name, **kwargs)

        if task not in ["binary", "multiclass", "regression"]:
            raise ValueError("task must be binary, multiclass or regression")

        self.task = task
        self.use_bias = use_bias
        self.num_class = num_class

    def build(self, input_shape):
        super().build(input_shape)

        if self.use_bias:
            self.global_bias = self.add_weight(
                shape=(self.num_class,) if self.task == "multiclass" else (1,),
                initializer=Zeros(), name="global_bias")

    def call(self, inputs, **kwargs):
        x = inputs

        if self.use_bias:
            x = tf.nn.bias_add(x, self.global_bias, data_format='NHWC')

        if self.task == "binary":
            x = tf.sigmoid(x)  # [[pred1], [pred2]]
            output = tf.reshape(x, (-1, 1))

        elif self.task == "multiclass":
            x = tf.nn.softmax(x)
            output = tf.reshape(x, (-1, self.num_class))

        else:
            # regression
            output = x

        return output

    def compute_output_shape(self, input_shape):
        if self.task == "multiclass":
            return (None, self.num_class)
        else:
            return (None, 1)

    def get_config(self, ):
        base_config = super().get_config()
        config = {'task': self.task, 'use_bias': self.use_bias, 'num_class': self.num_class}
        return {**base_config, **config}

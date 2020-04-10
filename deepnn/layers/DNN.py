#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : DNN
# @Time         : 2020-03-13 13:42
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import tensorflow as tf
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.initializers import Zeros, glorot_normal
from tensorflow.python.keras.layers import Layer
from tensorflow.python.keras.regularizers import l2


class DNN(Layer):

    def __init__(self, hidden_units, activation='relu', l2_reg=0, dropout_rate=0, use_bn=False, seed=1024, **kwargs):
        self.hidden_units = hidden_units
        self.activation = activation
        self.dropout_rate = dropout_rate
        self.seed = seed
        self.l2_reg = l2_reg
        self.use_bn = use_bn
        self.hidden_units_index = range(len(self.hidden_units))

        super(DNN, self).__init__(**kwargs)

    def build(self, input_shape):
        input_size = input_shape[-1]
        hidden_units = [int(input_size)] + list(self.hidden_units)

        # range(len(self.hidden_units))

        self.kernels = []
        self.bias = []

        for i in range(len(self.hidden_units)):
            kernel = self.add_weight(
                name='kernel' + str(i),
                shape=(hidden_units[i], hidden_units[i + 1]),
                initializer=glorot_normal(seed=self.seed),
                regularizer=l2(self.l2_reg),
                trainable=True
            )
            bias = self.add_weight(
                name='bias' + str(i),
                shape=(self.hidden_units[i],),
                initializer=Zeros(),
                trainable=True
            )

            self.kernels.append(kernel)
            self.bias.append(bias)

        if self.use_bn:
            self.bn_layers = [tf.keras.layers.BatchNormalization()] * len(self.hidden_units)

        self.dropout_layers = [tf.keras.layers.Dropout()] * len(self.hidden_units)

        self.activation_layers = [activation_layer(self.activation)] * len(self.hidden_units)

        super(DNN, self).build(input_shape)  # Be sure to call this somewhere! 传递信息？

    def call(self, inputs, training=None, **kwargs):

        deep_input = inputs
        for i in range(len(self.hidden_units)):
            fc = tf.nn.bias_add(tf.tensordot(deep_input, self.kernels[i], axes=(-1, 0)), self.bias[i])
            fc = self.bn_layers[i](fc, training=training) if self.use_bn else fc
            fc = self.activation_layers[i](fc)
            fc = self.dropout_layers[i](fc, training=training)
        return fc

    def compute_output_shape(self, input_shape):
        if len(self.hidden_units) > 0:
            shape = input_shape[:-1] + (self.hidden_units[-1],)
        else:
            shape = input_shape

        return tuple(shape)

    def get_config(self, ):
        config = {
            'activation': self.activation,
            'hidden_units': self.hidden_units,
            'l2_reg': self.l2_reg,
            'use_bn': self.use_bn,
            'dropout_rate': self.dropout_rate,
            'seed': self.seed
        }
        base_config = super(DNN, self).get_config()  # TODO: 更新配置信息
        return {**base_config, **config}
        # return dict(list(base_config.items()) + list(config.items()))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : demo
# @Time         : 2019-09-10 15:17
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

# coding=utf-8
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
import tensorflow.keras.backend as K

x_in = Input(shape=(784,))
x = x_in
x = Dense(100, activation='relu')(x)
x = Dense(784, activation='sigmoid')(x)

model = Model(x_in, x)
loss = K.mean((x - x_in) ** 2)
model.add_loss(loss)
model.compile(optimizer='adam') # from tensorflow_addons.optimizers import AdamW

model.summary()
# model.fit(x_train, None, epochs=5)



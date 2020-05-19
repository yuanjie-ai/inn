#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : __init__.py
# @Time         : 2020-03-12 12:48
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : https://github.com/wandb/client

import tensorflow as tf
import keras
import keras.backend as K
from keras.models import *
from keras.layers import *
from keras.layers import Input, Embedding, Dense, Dropout, BatchNormalization, Flatten, Concatenate, \
    Reshape, Activation
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, Callback

from keras.utils import np_utils

# from tensorflow.keras.datasets import fashion_mnist
# (X_train_orig, y_train_orig), (X_test, y_test) = fashion_mnist.load_data() # (60000, 28, 28)


from sklearn.datasets import make_regression, make_classification

X, y = make_classification(10240, 16)

# 789ae399af943555652e476ff1d0c0452ee86564
import wandb
from wandb.keras import WandbCallback  # torch

wandb.init(project="Keraser")
config = wandb.config

# Track hyperparameters
config.dropout = 0.2
config.hidden_layer_size = 128
config.layer_1_size = 16
config.layer_2_size = 32
config.learn_rate = 0.01
config.decay = 1e-6
config.momentum = 0.9
config.epochs = 8

input_shape = X.shape[1:]
input = Input(input_shape)
x = input
for i in [128, 64, 32, 16, 1]:
    x = Dense(i, activation='relu')(x)

output_model = Activation('sigmoid')(x)

model = Model(inputs=input, outputs=output_model)
model.summary()

model.compile('sgd', loss='binary_crossentropy', metrics=['accuracy', keras.metrics.AUC()])
model.fit(X, y, 128, 10)


tf.keras.losses.mean_squared_error,
import tensorflow_addons as tfa

tfa
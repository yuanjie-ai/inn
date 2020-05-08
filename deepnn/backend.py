#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : backend
# @Time         : 2019-09-10 15:16
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import tensorflow as tf

#
# from tensorflow.python import keras
#
# utils = keras.utils
# activations = keras.activations
# applications = keras.applications
# backend = keras.backend
# datasets = keras.datasets
# engine = keras.engine
# layers = keras.layers
# preprocessing = keras.preprocessing
# wrappers = keras.wrappers
# callbacks = keras.callbacks
# constraints = keras.constraints
# initializers = keras.initializers
# metrics = keras.metrics
# models = keras.models
# losses = keras.losses
# optimizers = keras.optimizers
# regularizers = keras.regularizers

custom_objects = {
    # metrics
    'auc': tf.keras.metrics.AUC

    # losses

    # optimizers

    # callbacks

    # layers

    # activations

    # 'Embedding': Embedding,
    # 'BiasAdd': BiasAdd,
    # 'MultiHeadAttention': MultiHeadAttention,
    # 'LayerNormalization': LayerNormalization,
    # 'PositionEmbedding': PositionEmbedding,
    # 'RelativePositionEmbedding': RelativePositionEmbedding,
    # 'RelativePositionEmbeddingT5': RelativePositionEmbeddingT5,
    # 'FeedForward': FeedForward,
    # 'ConditionalRandomField': ConditionalRandomField,
    # 'MaximumEntropyMarkovModel': MaximumEntropyMarkovModel,
    # 'Loss': Loss,
}

tf.keras.utils.get_custom_objects().update(custom_objects)

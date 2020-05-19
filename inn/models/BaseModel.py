#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : inn.
# @File         : BaseModel
# @Time         : 2020/5/19 2:24 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :

from abc import abstractmethod
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, Union

import tensorflow as tf
from tensorflow.python.feature_column.feature_column_v2 import \
    FeatureColumn, NumericColumn, CategoricalColumn, SequenceCategoricalColumn, EmbeddingColumn, \
    BucketizedColumn


class BaseModel(object):

    def __init__(self,  # todo: 初始化基础属性
                 feature_columns: List[FeatureColumn] = None,
                 task='binary',
                 num_class=None,
                 early_stopping_epochs=3):
        self.feature_columns = feature_columns
        self.task = task
        if task == 'multiclass':
            assert num_class is not None, "num_class must not be None"

        self.num_class = num_class
        self.early_stopping_epochs = early_stopping_epochs

    @abstractmethod
    def model(self):
        raise NotImplementedError()

    def compile(self,
                optimizer='rmsprop',
                loss=None,
                metrics=None,
                loss_weights=None,
                sample_weight_mode=None,
                weighted_metrics=None,
                target_tensors=None,
                distribute=None,
                **kwargs, ):
        self.model.compile(optimizer=optimizer,
                           loss=loss,
                           metrics=metrics,
                           loss_weights=loss_weights,
                           sample_weight_mode=sample_weight_mode,
                           weighted_metrics=weighted_metrics,
                           target_tensors=target_tensors,
                           distribute=distribute,
                           **kwargs, )

    def plot(self, to_file='model.png',
             show_shapes=False,
             show_layer_names=True,
             rankdir='TB',
             expand_nested=False,
             dpi=96):
        tf.keras.utils.plot_model(self.model, to_file=to_file,
                                  show_shapes=show_shapes,
                                  show_layer_names=show_layer_names,
                                  rankdir=rankdir,
                                  expand_nested=expand_nested,
                                  dpi=dpi)

    def callbacks(self):
        callbacks_list = [
            tf.keras.callbacks.ReduceLROnPlateau(factor=0.9, patience=2, verbose=1, min_lr=0.0001),
            # annealer = LearningRateScheduler(lambda x: min(0.01 * 0.9 ** x, 0.001), verbose=1)

            tf.keras.callbacks.ModelCheckpoint("filepath",
                                               monitor='val_loss',
                                               verbose=0,
                                               save_best_only=True,
                                               save_weights_only=False,
                                               mode='auto',
                                               save_freq='epoch'),

            tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                             min_delta=0,
                                             patience=self.early_stopping_epochs,
                                             verbose=0,
                                             mode='auto',
                                             baseline=None,
                                             restore_best_weights=False)
        ]
        return callbacks_list

    # todo: 学习率clr_callback, WandbCallback

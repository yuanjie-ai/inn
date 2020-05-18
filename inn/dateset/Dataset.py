#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : DataLoader
# @Time         : 2019-10-21 13:01
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
"""
cache
"""
import numpy as np
import pandas as pd
import tensorflow as tf

from pathlib import Path
from functools import partial


# TODO:
#  ds.repeat()?
#
class Dataset(object):
    """
    https://tensorflow.google.cn/guide/data?hl=zh_cn

    """

    def __init__(self, batchsize=128, cache_filename=""):
        self.batchsize = batchsize
        self.cache_filename = cache_filename

    def from_cache(self, X, y=None, shuffle_buffer_size=10000):
        """
        from sklearn.datasets import load_iris
        X, y = load_iris(True)

        :param X: (list, np.ndarray, dict, pd.DataFrame)
        :param y:
        :param shuffle_buffer_size:
        :return:
        """
        assert isinstance(X, (list, np.ndarray, dict, pd.DataFrame)), "Date Type Error"

        if isinstance(X, pd.DataFrame):
            X = X.to_dict('list')
        if y is None:
            tensors = X
        else:
            tensors = (X, y)

        # Common
        ds = tf.data.Dataset.from_tensor_slices(tensors)
        ds = ds.shuffle(shuffle_buffer_size, seed=None)
        ds = ds.batch(self.batchsize)
        ds = ds.prefetch(tf.data.experimental.AUTOTUNE)

        return ds


    def from_generator(self):
        # TODO: 增加对文件的操作（txt/tfrecord）
        # tf.data.Dataset.from_generator()
        pass

    def _from_np_array(self, array):
        # Common
        buffer_size = len(array)
        ds = tf.data.Dataset.from_tensor_slices(array)
        ds = ds.shuffle(buffer_size, seed=None)
        ds = ds.batch(self.batchsize)
        ds = ds.prefetch(tf.data.experimental.AUTOTUNE)

        return ds

    def _from_pd_dataframe(self, df: pd.DataFrame, label="label"):
        """
        import tensorflow as tf
        dataset = tf.data.Dataset.from_tensor_slices(({"a": [1, 2], "b": [3, 4]}, [0, 1]))
        print(list(dataset.as_numpy_iterator()))

        :param df:
        :param label:
        :return:
        """
        if label and label in df.columns:
            df = df.drop(labels=[label], axis=1)
            labels = df[label]
            tensors = (df.to_dict('list'), labels)  # df.to_dict('series')
        else:
            tensors = df.to_dict('list')

        # Common
        buffer_size = len(df)
        ds = tf.data.Dataset.from_tensor_slices(tensors)
        ds = ds.shuffle(buffer_size, seed=None)
        ds = ds.batch(self.batchsize)
        ds = ds.prefetch(tf.data.experimental.AUTOTUNE)

        # features_dataset = tf.data.Dataset.from_tensor_slices(features)
        # labels_dataset = tf.data.Dataset.from_tensor_slices(labels)
        # tf.data.Dataset.zip((features_dataset, labels_dataset))
        return ds


    def from_tfrecord(self, feature_dict: dict, file_pattern: str, file_shuffle=True, file_shuffle_seed=666,
                      shuffle_buffer_size=10000):
        """
        ds = Dataset()
        feature_dict = {
            'id': tf.io.FixedLenFeature((), tf.int64),
            'feature': tf.io.FixedLenFeature((), tf.int64)
            }
        ds = ds.from_tfrecord(feature_dict, '/Users/yuanjie/Desktop/Projects/Spark/MIPush/test-output.tfrecord/part*')

        :param feature_dict:
        :param file_pattern:
        :param shuffle:
        :param seed:
        :param shuffle_buffer_size:
        :return:
        """
        # TODO: cache
        # assert isinstance(filename, str), f"file path error: {filename}"
        #
        # if Path(filename).is_dir():
        #     filename = list(map(str, Path(filename).glob(glob_regex))) # tf.data.Dataset.list_files

        parser_fn = partial(tf.io.parse_single_example, features=feature_dict)
        filenames = tf.data.Dataset.list_files(file_pattern, file_shuffle, file_shuffle_seed)

        ds = (
            tf.data.TFRecordDataset(filenames, num_parallel_reads=tf.data.experimental.AUTOTUNE)
                .map(parser_fn)
                .shuffle(shuffle_buffer_size)
                .batch(self.batchsize)
                .prefetch(buffer_size=tf.data.experimental.AUTOTUNE)  # 若内存泄露，需手动指定
        )
        return ds


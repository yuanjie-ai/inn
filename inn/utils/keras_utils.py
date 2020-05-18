#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : keras_utils
# @Time         : 2020/4/21 8:22 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from tensorflow.keras import backend as K


def K_eval(x, backend=K):
    K = backend
    try:
        return K.get_value(K.to_dense(x))
    except Exception as e:
        try:
            eval_fn = K.function([], [x])
            return eval_fn([])[0]
        except Exception as e:
            return K.eager(K.eval)(x)

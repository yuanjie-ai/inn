#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : __init__.py
# @Time         : 2019-09-10 14:48
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :

from .pipe import *
from .logger import *
from .timer import timer
from .cprint import cprint
from .NT import NT

if os.environ.get('disable_eager_execution'):
    import tensorflow as tf

    tf.compat.v1.disable_eager_execution()
    logger.info('关闭动态图')


# from distutils.util import strtobool
# import numpy as np
# import tensorflow as tf
#
# # 判断是tf.keras还是纯keras的标记
# is_tf_keras = strtobool(os.environ.get('TF_KERAS', '0'))
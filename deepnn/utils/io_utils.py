#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : io_utils
# @Time         : 2020/4/21 12:04 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import os

get_module_path = lambda path, file=__file__: \
    os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(file), path))

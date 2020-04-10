#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : logger
# @Time         : 2020-04-10 16:35
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from loguru import logger
from pathlib import Path


def set_logger(log_cache=".", log_file_name="run.log"):
    logger.add(Path(log_cache) / log_file_name,
               rotation="100 MB",
               retention='1 days',
               encoding="utf-8",
               backtrace=True,
               diagnose=True,
               level="INFO")

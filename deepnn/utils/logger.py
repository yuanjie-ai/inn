#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : logger
# @Time         : 2020-04-10 16:35
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
import os
from loguru import logger
from pathlib import Path

LOG_PATH = os.environ.get("LOG_PATH")
if LOG_PATH:
    logger.add(Path(LOG_PATH),
               rotation="100 MB",
               retention='1 days',
               enqueue=True,  # 异步
               encoding="utf-8",
               backtrace=True,
               diagnose=True,
               level="INFO")

# import os
# import sys
# from loguru import logger
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# log_file_path = os.path.join(BASE_DIR, 'Log/my.log')
# err_log_file_path = os.path.join(BASE_DIR, 'Log/err.log')
#
# logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
# # logger.add(s)
# logger.add(log_file_path, rotation="500 MB", encoding='utf-8')  # Automatically rotate too big file
# logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8', level='ERROR')  # Automatically rotate too big file
# logger.debug("That's it, beautiful and simple logging!")
# logger.debug("中文日志可以不")
# logger.error("严重错误")

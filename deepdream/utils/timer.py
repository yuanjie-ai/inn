#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : timer
# @Time         : 2020-02-12 00:05
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
    # class MyResource:
    #     def query(self):
    #         print('query data')
    #
    # @contextmanager
    # def make_myresource():
    #     print('start to connect')
    #     yield MyResource()
    #     print('end connect')
    #     pass
    # with make_myresource() as r:
    #      r.query()
from skorch.helper import parse_args

import time
from contextlib import contextmanager
from deeptricks.utils import cprint

@contextmanager
def timer(task_name="timer"):
    print('\n')
    cprint(f"⏰ {task_name} started")
    t0 = time.time()
    yield
    cprint(f"⏰ {task_name} done in {time.time() - t0:.3f} seconds")


if __name__ == '__main__':
    with timer() as t:
        print('xxx')


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : pipe
# @Time         : 2020-04-10 16:41
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
from .cprint import cprint
from functools import update_wrapper
from tqdm.auto import tqdm


# 参照 tql_python
class pipe:
    """I am very like a linux pipe"""

    def __init__(self, function):
        self.function = function
        update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        return pipe(lambda x: self.function(x, *args, **kwargs))


# print
@pipe
def xprint(obj, mode=None, bg='blue'):
    if mode:
        for i in obj:
            cprint(i)
            print('\n')
    else:
        cprint(obj, bg)


xtqdm = pipe(lambda iterable, desc=None: tqdm(iterable, desc))

# base types
xtuple, xlist, xset = pipe(tuple), pipe(list), pipe(set)

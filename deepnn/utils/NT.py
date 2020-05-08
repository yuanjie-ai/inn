#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : get_namedtuple
# @Time         : 2020/4/13 12:04 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from . import namedtupled


class NT(object):

    def __new__(cls, _nt_name="NT", **kwargs):
        nt = namedtupled.map(kwargs, _nt_name=_nt_name)
        return nt


if __name__ == '__main__':
    class SF(NT):

        def __new__(cls, a='a', b='b'):

            return super().__new__(cls, a=a, b=b)
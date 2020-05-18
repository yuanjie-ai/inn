#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : hashtrick
# @Time         : 2020-04-10 16:54
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import hashlib as _hashlib
from sklearn.utils.murmurhash import murmurhash3_32 as _murmurhash3_32

"""Java
import java.nio.charset.StandardCharsets
import com.google.common.hash.Hashing.murmur3_32

def hash(key: String = "key", value: String = "value", bins: Int = 10000): Int = {
    val hashValue: Int = murmur3_32.newHasher.putString(f"{key}:{value}", StandardCharsets.UTF_8).hash.asInt
    Math.abs(hashValue) % bins  
  }
"""


def _md5(string: str):
    return _hashlib.md5(string.encode('utf8')).hexdigest()


def murmurhash(key="key", value="value", bins=None, str2md5=False):
    """key:value"""
    string = f"{key}:{value}"
    if str2md5:
        string = _md5(string)

    _ = abs(_murmurhash3_32(string))
    return _ % bins if bins else _


if __name__ == '__main__':
    print(_md5("key:value"))
    print(murmurhash())
    print(murmurhash(str2md5=True))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepTricks.
# @File         : cprint
# @Time         : 2020-02-12 00:09
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


def cprint(string='Hello World !', bg='blue', fg='', mode=1, return_str=False):
    """
    :param s: string
    :param fg/bg: foreground/background
        'black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'
    :param mode:
        0（默认值）
        1（高亮）
        22（非粗体）
        4（下划线）
        24（非下划线）
        5（闪烁）
        25（非闪烁）
        7（反显）
        27（非反显）
        https://www.cnblogs.com/hellojesson/p/5961570.html
    :return:
    """
    colors = ['green', 'yellow', 'black', 'cyan', 'blue', 'red', 'white', 'purple']
    fc = dict(zip(colors, range(40, 97)))
    bc = dict(zip(colors, range(90, 97)))
    _ = f"\033[{mode};{fc[fg]};{bc[bg]}m{string}\033[0m" if fg else f"\033[{mode};{bc[bg]}m{string}\033[0m"
    if return_str:
        return _
    else:
        print(_)


if __name__ == '__main__':
    cprint()

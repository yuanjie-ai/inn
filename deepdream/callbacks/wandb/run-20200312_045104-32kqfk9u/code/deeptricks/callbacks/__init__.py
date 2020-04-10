#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : __init__.py
# @Time         : 2020-03-12 12:48
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import wandb
from wandb.keras import WandbCallback

# Initialize wandb
wandb.init(project="example")
config = wandb.config
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : __init__.py
# @Time         : 2020-03-12 12:48
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import tensorflow.keras
import wandb
from wandb.keras import WandbCallback

# torch
# Initialize wandb
wandb.init(project="Keraser")
config = wandb.config

# Track hyperparameters
config.dropout = 0.2
config.hidden_layer_size = 128
config.layer_1_size = 16
config.layer_2_size = 32
config.learn_rate = 0.01
config.decay = 1e-6
config.momentum = 0.9
config.epochs = 8

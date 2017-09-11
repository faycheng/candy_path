# -*- coding:utf-8 -*-

import os


def mkdirs(path):
    if os.path.exists(path) and os.path.isdir(path):
        return
    os.makedirs(path)



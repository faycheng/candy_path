# -*- coding:utf-8 -*-

import os


def mkdirs(path):
    if os.path.exists(path) and os.path.isdir(path):
        return
    os.makedirs(path)


def touch(path):
    if os.path.exists(path) and os.path.isfile(path):
        return
    fd = open(path, 'w')
    fd.close()



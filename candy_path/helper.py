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


def get_parent_path(path, depth=1):
    parent_path = path
    for _ in range(depth):
        parent_path = os.path.abspath(os.path.dirname(parent_path))
    return parent_path
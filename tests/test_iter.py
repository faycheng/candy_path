# -*- coding:utf-8 -*-
import os
import shutil
import types
import candy_path

from candy.utils import faker
from candy_path import helper
from candy_path import iter


def test_list_dirs():
    path = os.path.join(candy_path.CWD, faker.random_string())
    sub_dir = os.path.join(path, faker.random_string())
    helper.mkdirs(sub_dir)

    dirs = iter.list_dirs(path, recursion=False)
    assert isinstance(dirs, types.GeneratorType)
    dirs = list(dirs)
    assert len(dirs) == 1
    assert sub_dir in dirs
    shutil.rmtree(path)

    path = os.path.join(candy_path.CWD, faker.random_string())
    sub_dir = os.path.join(path, faker.random_string())
    grand_dir = os.path.join(sub_dir, faker.random_string())
    helper.mkdirs(grand_dir)

    dirs = iter.list_dirs(path, recursion=True)
    assert isinstance(dirs, types.GeneratorType)
    dirs = list(dirs)
    assert len(dirs) == 2
    assert sub_dir in dirs
    assert grand_dir in dirs
    shutil.rmtree(path)

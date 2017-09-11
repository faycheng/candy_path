# -*- coding:utf-8 -*-

import os
import pytest

import candy_path
from candy.utils import faker
from candy_path import helper


def test_mkdirs():
    path = os.path.join(candy_path.CWD, faker.random_string())
    helper.mkdirs(path)
    assert os.path.exists(path)
    os.rmdir(path)

    path_0 = os.path.join(candy_path.CWD, faker.random_string())
    path_2 = os.path.join(path_0, faker.random_string())
    helper.mkdirs(path_2)
    assert os.path.exists(path_2)

    helper.mkdirs(path_2)
    os.rmdir(path_2)
    os.rmdir(path_0)

    path = os.path.join(candy_path.CWD, faker.random_string())
    helper.touch(path)
    with pytest.raises(FileExistsError):
        helper.mkdirs(path)
    os.remove(path)


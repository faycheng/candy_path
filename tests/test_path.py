# -*- coding:utf-8 -*-

import os
import pytest
from candy_path.helper import touch
from candy_path import CWD
from candy.utils import faker
from candy_path.path import Path


def test_path_init():
    with pytest.raises(IOError):
        Path(faker.random_string())

    p = os.path.join(CWD, faker.random_string())
    os.mkdir(p)
    Path(p)
    os.rmdir(p)


def test_path_parent_dir():
    p = os.path.join(CWD, faker.random_string())
    os.mkdir(p)
    p = Path(p)
    assert p.parent_dir == CWD
    os.rmdir(p.abs_path)


def test_path_is_dir():
    p = os.path.join(CWD, faker.random_string())
    os.mkdir(p)
    p = Path(p)
    assert p.is_dir is True
    os.rmdir(p.abs_path)

    p = os.path.join(CWD, faker.random_string())
    touch(p)
    p = Path(p)
    assert p.is_dir is False
    os.remove(p.abs_path)


def test_path_is_file():
    p = os.path.join(CWD, faker.random_string())
    os.mkdir(p)
    p = Path(p)
    assert p.is_file is False
    os.rmdir(p.abs_path)

    p = os.path.join(CWD, faker.random_string())
    touch(p)
    p = Path(p)
    assert p.is_file is True
    os.remove(p.abs_path)


def test_path_name():
    n = faker.random_string()
    p = os.path.join(CWD, n)
    os.mkdir(p)
    p = Path(p)
    assert p.name == n
    os.rmdir(p.abs_path)


def test_path_extension_name():
    p = os.path.join(CWD, faker.random_string(), '.py')
    touch(p)
    p = Path(p)
    assert p.extension_name == 'py'
    os.remove(p.abs_path)

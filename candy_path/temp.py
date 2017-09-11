# -*- coding:utf-8 -*-

import os


class TempDir(object):
    pass


class TempFile(object):
    def __init__(self, name=None, suffix='tmp'):
        self.path = '/tmp/{}.{}'.format(name or str(uuid.uuid4()), suffix)
        self._fd = None
        self._close = False

    @property
    def fd(self):
        if self._fd is None:
            self._fd = open(self.path, 'w')
        return self._fd

    def close(self):
        if self._close is True:
            return
        self.fd.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        os.remove(self.path)




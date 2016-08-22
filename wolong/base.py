import pandas as pd

import os.path
import hashlib
import logging

LOG = logging.getLogger(__name__)

DEFAULT_CACHE_DIR = ".labcache"
DEFAULT_DB_FILENAME = "lab.db"

class BaseLab(object):
    _cursor_bucket = 'cursor'

    def __init__(self, cache_dir, data_store):
        self._cache_dir = os.path.abspath(cache_dir)
        self._data_store = data_store

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._data_store.close()

    @property
    def buckets(self):
        return self._data_store

    @property
    def cursor(self):
        return self._data_store[self._cursor_bucket]

    @cursor.setter
    def cursor(self, value):
        self._data_store[self._cursor_bucket] = value

    def get_filename(self, infile_name):
        with open(infile_name, 'rb') as infile:
            _h = hashlib.md5(infile.read()).hexdigest()
        return os.path.join(self._cache_dir, _h)

    @cursor.setter
    def files(self):
        raise NotImplementedError()

    @classmethod
    def from_dir(cls, cache_dir, filename=None):
        if filename is None:
            filename = os.path.join(cache_dir, DEFAULT_DB_FILENAME)
        return cls(cache_dir, pd.io.pytables.HDFStore(filename))

class BasePlugin(object):
    consumes_cols = None
    provides_cols = None

    def __init__(self, df):
        assert self.consumes_cols is not None
        assert isinstance(self.consumes_cols, list)
        assert self.provides_cols is not None
        assert isinstance(self.provides_cols, list)
        df = self._filter_columns(df)
        self._df = df

    @classmethod
    def _filter_columns(cls, df):
        return df

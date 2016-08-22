# -*- coding: utf-8 -*-

__author__ = 'Brian Rossa'
__email__ = 'brian.rossa@gmail.com'
__version__ = '0.0.1'

LABEL_BUCKET_NAME = 'labels'
TEMPORARY_COL_NAME = '__index'

from .entrypoints import *

def save(self, save_name, merge_method=None, labels=None):
    _c = self._cursor
    # _c[self.TEMPORARY_COL_NAME] = True
    if merge_method == 'concat':
        old_df = self._get_node(save_name)
        _c = pd.concat([old_df, _c]).reset_index(drop=True)
    elif merge_method == 'join':
        old_df = self._get_node(save_name)
        cols = [c for c in _c.columns if c in old_df.columns]
        if len(cols) > 0:
            old_df = old_df.drop(cols, axis=1)
            _c = old_df.join(_c)
    elif merge_method == 'assign':
        old_df = self._get_node(save_name)
        if isinstance(_c, pd.DataFrame):
            cols = [c for c in _c.columns if c in old_df.columns]
        elif isinstance(_c, pd.Series):
            cols = [c for c in [_c.name] if c in old_df.columns]
        else:
            raise Exception()
        if len(cols) > 0:
            old_df = old_df.drop(cols, axis=1)
        if isinstance(_c, pd.DataFrame):
            old_df[_c.columns] = _c
        elif isinstance(_c, pd.Series):
            old_df[_c.name] = _c
        else:
            raise Exception()
        _c = old_df
        # self._cursor = _c
        # if labels is not None:
        #     for _l in labels:
        #         self.label(_l, save_name, self.TEMPORARY_COL_NAME)
        # self._cursor.drop(self.TEMPORARY_COL_NAME, axis=1, inplace=True)
        # print(save_name, self._data_store, _c)
    self._data_store[save_name] = _c

# TODO not working
# def cli_label(self, arg_ns, arg_parser):
#     self.label(arg_ns.label, arg_ns.table_name)

def label(self, label, table_name, filter_col):
    cursor_df = self._cursor.reset_index()
    cursor_df['label'] = label
    cursor_df['table'] = table_name
    new_label_df = cursor_df[['table', filter_col, 'label']]
    new_label_df.columns = ['table', 'index', 'label']
    if self.LABEL_BUCKET_NAME in self._data_store:
        old_label_df = self._get_node(self.LABEL_BUCKET_NAME)
        new_label_df = pd.concat([old_label_df,
                                  new_label_df]).reset_index(drop=True)
        self._data_store[self.LABEL_BUCKET_NAME] = new_label_df

def query_filter(self, query_str):
    df = self._cursor
    locs = df.to_dict(orient='series')
    mask = eval(query_str, {}, locs).as_matrix()
    new_frame = df[mask]
    self._cursor = new_frame

def query_label(self, label):
    label_df = self._get_node('labels')
    label_df = label_df[label_df['label']==label]
    unique_tables = label_df['table'].unique()
    assert len(unique_tables) == 1
    table = unique_tables[0]
    indices = label_df['index']
    data_df = self._get_node(table).iloc[indices]
    self._cursor = data_df

def apply(self, arg_ns, arg_parser):
    df = self._get_node(arg_ns.apply_node)
    if arg_ns.use_exec:
        raise NotImplementedError()
    else:
        func = eval(arg_ns.func_str, EVAL_NAMESPACE, {})
    if arg_ns.pandas:
        result = func(df)
        if isinstance(result, pd.Series):
            result.name = arg_ns.name
    elif arg_ns.axis is None:
        result = pd.DataFrame({arg_ns.name: func(df)},
                              index=df.index)
    else:
        result = df.apply(func, axis=arg_ns.axis)
    if arg_ns.show:
        print(result)
        self._cursor = result

def merge_apply(self, arg_ns, arg_parser):
    point_df = self._get_node(arg_ns.point_node)
    edge_df = self._get_node(arg_ns.edge_node)
    merge_df = cloudlab.pandas_helpers.double_merge(point_df, edge_df)
    if arg_ns.use_exec:
        raise NotImplementedError()
    else:
        func = eval(arg_ns.func_str, EVAL_NAMESPACE, {})
    if arg_ns.axis is None:
        result = pd.DataFrame({arg_ns.name: func(merge_df)},
                              index=merge_df.index)
    else:
        result = merge_df.apply(func, axis=arg_ns.axis)
    if arg_ns.show:
        print(results)
        self._cursor = result

def drop_duplicates(self, arg_ns, arg_parser):
    df = self._get_node(arg_ns.node_name)
    self._cursor = df.drop_duplicates()

def _get_node(self, node_name):
    return self._data_store[node_name]

def _set_node(self, node_name, data):
    self._data_store[node_name] = data

# def __del__(self):
#     self.save_cursor()

def save_cursor(self):
    LOG.debug('>>>>>', self._data_store, "{", self._data_store.is_open, "}")
    if self._cursor is not None:
        self._set_node('cursor', self._cursor)
        self._data_store.close()

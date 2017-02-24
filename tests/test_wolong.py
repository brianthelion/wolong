#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_wolong
----------------------------------

Tests for `wolong` module.
"""


import sys
import unittest

class TestWolong(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic_imports(self):
        import wolong.plugins
        from wolong import plugins
        from wolong.plugins import entrypoints

if __name__ == '__main__':
    sys.exit(unittest.main())

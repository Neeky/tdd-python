#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


class TestRaiseExceptionTestCase(unittest.TestCase):
    def test_raise_exception(self):
        # 断言这里会报异常
        with self.assertRaises(Exception):
            mock = MagicMock(side_effect=Exception("Boom!"))
            mock()


if __name__ == "__main__":
    unittest.main()

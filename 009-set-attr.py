#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


class TestFoo(unittest.TestCase):
    def test_set_attr(self):
        expected = "tom"
        mm = MagicMock()
        mm.name = "tom"

        self.assertEqual(mm.name, expected)

    def test_set_attr_complex(self):
        expected = ("hello", "world")

        mock = MagicMock()
        cursor = mock.connection.cursor.return_value
        cursor.execute.return_value = ("hello", "world")
        res = mock.connection.cursor().execute("select xx, xx ;")
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()

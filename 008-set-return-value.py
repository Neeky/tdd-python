#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


class TestFoo(unittest.TestCase):
    def test_set_return_value(self):
        expected = 100
        mock = MagicMock()
        mock.return_value = 100

        self.assertEqual(mock(), expected)


if __name__ == "__main__":
    unittest.main()

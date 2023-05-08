#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


def side_effect():
    return "hello world"


class TestSideEffectTestCase(unittest.TestCase):
    def test_side_effect(self):
        mock = MagicMock(side_effect=side_effect)
        expected = "hello world"
        res = mock()
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


class TestSideEffectTestCase(unittest.TestCase):
    def test_side_effect(self):
        mock = MagicMock(side_effect=[1, 10, 100, 1000])
        expected = 1
        res = mock()
        self.assertEqual(res, expected)

        expected = 10
        res = mock()
        self.assertEqual(res, expected)

        expected = 100
        res = mock()
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()

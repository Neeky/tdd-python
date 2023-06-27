#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel, mock_open, Mock


class IterTestCase(unittest.TestCase):
    def test_iter(self):
        mock = Mock(side_effect=[100, 200, 300])

        expected = 100
        self.assertEqual(expected, mock())

        expected = 200
        self.assertEqual(expected, mock())

        expected = 300
        self.assertEqual(expected, mock())


if __name__ == "__main__":
    unittest.main()

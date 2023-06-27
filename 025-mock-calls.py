#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel, mock_open


class MockCallsTestCase(unittest.TestCase):
    """
    mock 的调用参数检查
    """

    def test_mock_calls(self):
        mock = MagicMock()
        mock("tom")
        mock("jerry")
        expected = [call("tom"), call("jerry")]
        self.assertEqual(expected, mock.mock_calls)


if __name__ == "__main__":
    # read_hosts()
    unittest.main()

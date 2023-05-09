#!/usr/bin/env python3
#! -*- encoding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel


class TestOpen(unittest.TestCase):
    def test_patch_open(self):
        mock = MagicMock(return_value=sentinel.file_handle)
        with patch("builtins.open", mock):
            handle = open("filename", "r")
        mock.assert_called_once_with("filename", "r")
        self.assertEqual(handle, sentinel.file_handle)

    def test_patch_open_v2(self):
        with patch("builtins.open") as mock:
            mock.return_value.read.return_value = "abc"
            handle = open("filename", "r")
            res = handle.read()
        mock.assert_called_once_with("filename", "r")
        self.assertEqual(res, "abcd")


if __name__ == "__main__":
    unittest.main()

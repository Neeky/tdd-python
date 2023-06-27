#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel, mock_open, Mock


def foo(s):
    return "xxx"


class ReturnValuesTestCase(unittest.TestCase):
    """ """

    def test_return_values(self):
        """
        定制 mock 调用的返回值
        """
        # 第一步    设计好一个输入参数与返回值的对应关系
        args_to_values = {"foo": "bar", "hello": "world"}

        # 第二步    设计一个 side_effect 函数，来处理这种对应关系
        def side_effect(k):
            return args_to_values[k]

        # 第三步    使用刚才的 side_effect 函数
        mock = Mock(side_effect=side_effect)
        expected = "bar"
        self.assertEqual(expected, mock("foo"))

        expected = "world"
        self.assertEqual(expected, mock("hello"))


if __name__ == "__main__":
    unittest.main()

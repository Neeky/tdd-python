#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


def tool_func():
    from datetime import datetime

    with open("/tmp/a.txt", "wa") as f:
        f.write(datetime.now().isoformat())


class Foo(object):
    def fun():
        return "hello wrold"


class TestMockAnExistsObject(unittest.TestCase):
    def test_mock_an_exists_fun(self):
        """"""
        mock = MagicMock(spec=tool_func)
        mock()
        self.assertTrue(mock.called)
        mock.assert_called_once()
        mock.assert_called_once_with()

    def test_mock_an_exists_object(self):
        """ """
        expected = "hello world"
        mock = MagicMock(spec=Foo)
        result = mock.fun()
        mock.fun.assert_called_once()
        """
        这里的 bat 调用会失败，原因是 Foo 中并没有这个函数
        """
        # mock.bat()


if __name__ == "__main__":
    unittest.main()

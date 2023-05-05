#! -*- encoding: utf8 -*-

# from util import Foo

import util
import unittest
from unittest.mock import patch


def some_function():
    # 相比 002 来说, Foo 在这里不是通过传参得到的，而是直接写死的
    # 这种情况下我们只能用是 patch 了
    foo = util.Foo()
    return foo.get_id()


class TestFoo(unittest.TestCase):
    """ """

    def test_foo(self):
        with patch("util.Foo") as mock:
            instance = mock.return_value
            instance.get_id.return_value = 10086
            result = some_function()
            self.assertEqual(result, 10086)


if __name__ == "__main__":
    unittest.main()

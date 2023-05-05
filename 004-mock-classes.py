#! -*- encoding: utf8 -*-

from util import Foo
import unittest
from unittest.mock import patch


def some_function():
    # 相比 003 来说, Foo 是直接引用的，而不是通过 util.Foo 引用的，这个就会导致 patch 不了
    foo = Foo()
    return foo.get_id()


class TestFoo(unittest.TestCase):
    """如果导入对象的时间没有带上包名、这个会导致我们 patch 不了，进而不好测试。"""

    def test_foo(self):
        with patch("util.Foo") as mock:
            instance = mock.return_value
            instance.get_id.return_value = 10086
            result = some_function()
            # 这里会断言失败 result 会是 'foo'
            self.assertEqual(result, 10086)


if __name__ == "__main__":
    unittest.main()

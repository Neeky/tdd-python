#! -*- encoding: utf8 -*-

import util
import unittest

# 这一行需要、不然后面的 with 语句会报错， 不确认是不是版本问题
# python3 --version
# Python 3.11.2
from unittest.mock import MagicMock


def some_function():
    return util.bar()


class TestBar(unittest.TestCase):
    def test_bar(self):
        with unittest.mock.patch("util.bar") as mock:
            mock.return_value = "bu bu bu!"
            result = some_function()
            self.assertEqual(result, "bu bu bu!")


if __name__ == "__main__":
    unittest.main()

#! -*- encoding:utf8 -*-

import unittest
from unittest.mock import MagicMock


def foo():
    return "this is foo function ."


class Person(object):
    def do_somthing(self, func):
        """ """
        return func()


class TestPerson(unittest.TestCase):
    def test_do_somthing(self):
        """ """
        person = Person()
        expect = "this is mock function ."
        mkf = MagicMock(return_value=expect)
        # 要把被依赖的函数换成 mock 对象传进去
        result = person.do_somthing(mkf)

        self.assertEqual(result, expect)
        mkf.assert_called_once()
        mkf.assert_called


if __name__ == "__main__":
    unittest.main()

#! -*- encoding:utf8 -*-

import unittest
from unittest.mock import MagicMock


class Person(object):
    name = "tom"

    def say_hello(self):
        print("Hello My name is {} .".format(self.name))


class TestPerson(unittest.TestCase):
    def test_person(self):
        expect = "hello unittest"
        tom = Person()
        tom.say_hello = MagicMock(return_value=expect)
        result = tom.say_hello()
        # 断言调用的时候没有带参数
        tom.say_hello.assert_called_once_with()
        # 断言已经调用过
        self.assertTrue(tom.say_hello.called)
        # 断言返回值，与我们期望的一样
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main()

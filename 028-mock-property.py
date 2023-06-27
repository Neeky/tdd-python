#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import (
    MagicMock,
    call,
    patch,
    sentinel,
    mock_open,
    Mock,
    PropertyMock,
)


class Person(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class PersonTestCase(unittest.TestCase):
    def test_name_property(self):
        with patch("__main__.Person.name", new_callable=PropertyMock) as mock_name:
            mock_name.return_value = "cat"
            cat = Person("xxx")
            expected = "cat"

            self.assertEqual(expected, cat.name)

            cat.name = "dog"
            # 由于前面设置了 mock_name.return_value = "cat" 的原因
            # 就算这里设置了 cat.name = "dog", 实际的返回值也会是 "cat"
            expected = "cat"
            self.assertEqual(expected, cat.name)


if __name__ == "__main__":
    # tom = Person("tom")
    # print(tom.name)
    # tom.name = "jerry"
    # print(tom.name)
    unittest.main()

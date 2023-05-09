#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call, patch, sentinel

from util import Foo


class TestFoo(unittest.TestCase):
    @patch.object(Foo, "id", sentinel.attribute)
    def test_foo(self):
        self.assertEqual(Foo.id, sentinel.attribute)
        print(sentinel.attribute)
        print(sentinel.attribute)
        print(sentinel.attribute)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
#! -*- encoding: utf8 -*-

import unittest
from unittest.mock import MagicMock, call


def tool_func():
    from datetime import datetime

    with open("/tmp/a.txt", "wa") as f:
        f.write(datetime.now().isoformat())


class TestMockAnExistsObject(unittest.TestCase):
    def test_mock_an_exists_object(self):
        """"""
        mock = MagicMock(spec=tool_func)
        mock()
        self.assertTrue(mock.called)
        mock.assert_called_once()
        mock.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()

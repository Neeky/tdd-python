#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel

from pathlib import Path


def fun():
    instance = Path("/tmp")
    return instance.exists()


class PathTestCase(unittest.TestCase):
    def test_fun(self):
        with patch.object(Path, "exists") as mock_exists:
            mock_exists.return_value = False
            result = fun()
            self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()

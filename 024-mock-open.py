#!/usr/bin/env python3
#! -*- coding: utf8 -*-


import unittest
from unittest.mock import MagicMock, call, patch, sentinel, mock_open
from util import read_hosts


class OpenTestCase(unittest.TestCase):
    """ """

    def test_open(self):
        """ """
        with patch("__main__.open", mock_open(read_data="bibble")) as mock:
            with open("/tmp/xxx") as x_file:
                for line in x_file:
                    with self.assertRaises(ValueError):
                        if line == "bibble":
                            raise ValueError(line)

        mock.assert_called_with("/tmp/xxx")

        pass


if __name__ == "__main__":
    # read_hosts()
    unittest.main()

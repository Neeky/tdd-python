#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock, call


class TestFoo(unittest.TestCase):
    """"""

    def test_tracking_all_calls(self):
        mm = MagicMock()
        mm.hello()
        mm.attr.world()

        print(mm.mock_calls)

        c, cc = mm.mock_calls  # [call.hello(), call.attr.world()]
        self.assertEqual(c, call.hello())


if __name__ == "__main__":
    unittest.main()

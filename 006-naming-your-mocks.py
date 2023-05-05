#! -*- encoding: utf8 -*-

import util
import unittest
from unittest.mock import MagicMock


def main():
    named_mock = MagicMock(name="my_mock")
    # 创建的时候有传 name , 在 print 的时候就能看到
    print(named_mock)  # <MagicMock name='my_mock' id='xxxx'>


if __name__ == "__main__":
    main()

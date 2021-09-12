import unittest
from abc import ABCMeta
import os
import sys
sys.path.append(os.path.abspath(".."))

from src.templator.ITemplator import ITemplator

class BaseTemplatorTest(unittest.TestCase, metaclass=ABCMeta):
    pass

if __name__ == '__main__':
    unittest.main()

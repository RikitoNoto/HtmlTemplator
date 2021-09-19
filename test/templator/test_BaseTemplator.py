import unittest
from abc import ABCMeta
import os
import sys
sys.path.append(os.path.abspath("../.."))

from src.templator.BaseTemplator import BaseTemplator

class BaseTemplatorTest(unittest.TestCase, metaclass=ABCMeta):

    class BaseTemplatorStub(BaseTemplator):
        def render(self, *args, **kwargs):
            pass

    def setUp(self) -> None:
        self.set_instance("")

    def tearDown(self) -> None:
        self.instance = None

    def set_instance(self, *args, **kwargs)->BaseTemplatorStub:
        self.instance = self.BaseTemplatorStub(*args, **kwargs)
        return self.instance

    def test_should_be_set_datas(self):
        try:
            self.instance.datas = {"data": "data"}
        except:
            self.fail("could not set data.")

    def test_should_be_get_datas(self):
        self.assertEqual(self.instance.datas, dict())

    def test_should_be_get_set_datas(self):
        datas = {"test": "ok"}
        self.instance.datas = datas
        self.assertEqual(self.instance.datas, datas)

    def test_should_be_set_source(self):
        try:
            self.instance.source = "source"
        except:
            self.fail("could not set data.")

    def test_should_be_get_source(self):
        self.assertEqual(self.instance.source, "")

    def test_should_be_get_set_source(self):
        source = "source"
        self.instance.source = source
        self.assertEqual(self.instance.source, source)

    def test_should_be_get_data(self):
        self.assertEqual(self.instance.get_data("data"), "")

    def test_should_be_get_set_data(self):
        data = "data"
        self.instance.set_data(data, data)
        self.assertEqual(self.instance.get_data(data), data)

if __name__ == '__main__':
    unittest.main()

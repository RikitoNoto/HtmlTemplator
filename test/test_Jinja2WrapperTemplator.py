import unittest
import os
import sys
sys.path.append(os.path.abspath(".."))

from src.templator.Jinja2WrapperTemplator import Jinja2WrapperTemplator

class Jinja2WrapperTemplatorTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance:Jinja2WrapperTemplator = None

    def setUp(self) -> None:
        self.set_instance("")

    def tearDown(self) -> None:
        self.instance = None

    def set_instance(self, *args, **kwargs)->Jinja2WrapperTemplator:
        self.instance = Jinja2WrapperTemplator(*args, **kwargs)
        return self.instance

    def test_should_create_instance_with_string(self):
        try:
            self.set_instance("")
        except:
            self.fail("could not create instance.")

    def test_should_be_render_with_dict(self):
        try:
            self.instance.render({})
        except:
            self.fail("could not render")

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

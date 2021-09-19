import unittest
import os
import sys
sys.path.append(os.path.abspath("../.."))

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

if __name__ == '__main__':
    unittest.main()

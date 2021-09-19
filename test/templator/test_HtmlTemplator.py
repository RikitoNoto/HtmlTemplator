import unittest
from unittest.mock import MagicMock
import os
import sys
sys.path.append(os.path.abspath("../.."))

from src.templator.HtmlTemplator import HtmlTemplator
from src.templator.ITemplator import ITemplator

class TestHtmlTemplator(unittest.TestCase):

    def setUp(self) -> None:
        self.set_templator_spy(klass=ITemplator)
        self.set_html_templator(self.__templator_spy)

    def tearDown(self) -> None:
        del self.__html_templator
        del self.__templator_spy

    def set_templator_spy(self, klass=ITemplator):
        self.__templator_spy = MagicMock(spec=klass)
        return self.__templator_spy

    def set_html_templator(self, library_wrapper:type):
        self.__html_templator = HtmlTemplator(library_wrapper)
        return self.__html_templator


    def test_should_be_output_empty(self):
        self.__templator_spy.return_value.render.return_value = ""
        self.__html_templator.source = ""
        output = self.__html_templator.render()
        self.assertEqual(output, "")

    def test_should_be_output_html_no_change(self):
        render_output = "<html></html>"
        self.__html_templator.source = render_output
        self.__templator_spy.return_value.render.return_value = render_output
        self.assertEqual(self.__html_templator.render(), render_output)

if __name__ == '__main__':
    unittest.main()

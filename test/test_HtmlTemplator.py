import unittest
import os
import sys
sys.path.append(os.path.abspath(".."))

from src.HtmlTemplator import HtmlTemplator

class TestHtmlTemplator(unittest.TestCase):
    def test_should_be_output_empty(self):
        output = HtmlTemplator("").compile()
        self.assertEqual(output, "")

    def test_should_be_output_html_no_change(self):
        output = HtmlTemplator("<html></html>").compile()
        self.assertEqual(output, "<html></html>")

    def test_should_be_output_html_from_jinja_template(self):
        output = HtmlTemplator("<html>{{name}}</html>").compile(datas={"name":"success"})
        self.assertEqual(output, "<html>success</html>")

if __name__ == '__main__':
    unittest.main()

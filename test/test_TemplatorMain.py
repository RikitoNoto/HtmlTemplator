import unittest
import sys
import os
sys.path.append(os.path.abspath(".."))

import src.TemplatorMain as main

class TemplatorMainTest(unittest.TestCase):

    def test_should_be_not_skip_with_no_arg(self):
        self.assertFalse(main.is_name_skip("context", ""))

    def test_should_be_no_skip_with_not_match(self):
        self.assertFalse(main.is_name_skip("context_", "^_"))

    def test_should_be_skip_with_match(self):
        self.assertTrue(main.is_name_skip("_context", "^_"))

    def test_should_be_not_skip_prefix_with_no_arg(self):
        self.assertFalse(main.is_name_skip_with_prefix("context", ""))

    def test_should_be_no_skip_prefix_with_not_match(self):
        self.assertFalse(main.is_name_skip_with_prefix("context_", "_"))

    def test_should_be_skip_prefix_with_match(self):
        self.assertTrue(main.is_name_skip_with_prefix("_context", "_"))

    def test_should_be_not_skip_suffix_with_no_arg(self):
        self.assertFalse(main.is_name_skip_with_suffix("context", ""))

    def test_should_be_no_skip_suffix_with_not_match(self):
        self.assertTrue(main.is_name_skip_with_suffix("context_", "_"))

    def test_should_be_skip_suffix_with_match(self):
        self.assertFalse(main.is_name_skip_with_suffix("_context", "_"))

if __name__ == '__main__':
    unittest.main()

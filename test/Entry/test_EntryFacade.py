import unittest
from TestUtility import TestUtility
import os
import sys
sys.path.append(os.path.abspath("../.."))

from src.Entry.EntryFacade import EntryFacade
from src.Entry.Entry import EntryIF
from src.Entry.Entry import File
from src.Entry.Entry import Directory
from src.Entry.Entry import Link
from src.Entry.Entry import Device


class EntriesFacadeTest(unittest.TestCase, TestUtility):

    def test_should_make_file_no_content_no_reflect(self):
        file = EntryFacade.make(path="", content=("",), reflect=False)
        correct_file = File()
        correct_file.name = ""
        correct_file.path = ""
        correct_file.contents = []
        self.is_same_entry(file, correct_file)


if __name__ == '__main__':
    unittest.main()

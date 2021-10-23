import unittest
from test_EntryBase import EntryBaseTest
from TestUtility import TestUtility
import os
import sys
sys.path.append(os.path.abspath("../.."))

from src.Entry.Entry import *


class EntriesFileTest(EntryBaseTest, TestUtility):
    DEFAULT_DIRECTORY_PATH = "./temp"
    DEFAULT_FILE_NAME = "temp_file"
    INSTANCE_CLASS = File
    DEFAULT_PATH = os.path.join(DEFAULT_DIRECTORY_PATH, DEFAULT_FILE_NAME)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = self.DEFAULT_PATH

    def setUp(self) -> None:
        super().setUp()
        self.create_file(path=self.DEFAULT_PATH, content="")

    def tearDown(self) -> None:
        super().tearDown()
        self.delete_file(path=self.DEFAULT_PATH)

    def test_should_be_reflect_file_name(self):
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.name, os.path.basename(self.path))

    def test_should_be_reflect_file_no_content(self):
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.contents[File.FILE_CONTENT_INDEX], "")

    def test_should_be_reflect_file_with_content(self):
        content = "test"
        self.write_file_content(path=self.DEFAULT_PATH, content=content)
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.contents[File.FILE_CONTENT_INDEX], content)


class EntriesDirectoryTest(EntryBaseTest, TestUtility):
    DEFAULT_DIRECTORY_PATH = "."
    DEFAULT_DIRECTORY_NAME = "temp"
    INSTANCE_CLASS = Directory
    DEFAULT_PATH = os.path.join(DEFAULT_DIRECTORY_PATH, DEFAULT_DIRECTORY_NAME)
    DEFAULT_SUB_DIRECTORY_NAME = ("test1", "test2", "test3")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = self.DEFAULT_PATH

    def setUp(self) -> None:
        super().setUp()
        self.create_directory(path=self.DEFAULT_PATH, sub_directory_names=())

    def tearDown(self) -> None:
        super().tearDown()
        self.delete_directory(path=self.DEFAULT_PATH)

    def test_should_be_reflect_directory_name(self):
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.name, os.path.basename(self.path))

    def test_should_be_reflect_file_no_content(self):
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.contents, [])

    def test_should_be_reflect_file_with_content(self):
        sub_directory_names = self.DEFAULT_SUB_DIRECTORY_NAME
        self.create_sub_directory(path=self.DEFAULT_PATH, sub_directory_names=sub_directory_names)
        self.instance.path = self.path
        self.instance.reflect()
        for name in sub_directory_names:
            if name not in self.instance.contents:
                self.fail()


if __name__ == '__main__':
    unittest.main()

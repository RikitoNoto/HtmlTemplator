import unittest
from test_EntryBase import EntryBaseTest
import os
import sys
import shutil
sys.path.append(os.path.abspath("../.."))

from src.Entry.Entry import *


class EntriesFileTest(EntryBaseTest):
    DEFAULT_DIRECTORY_PATH = "./temp"
    DEFAULT_FILE_NAME = "temp_file"
    INSTANCE_CLASS = File
    DEFAULT_PATH = os.path.join(DEFAULT_DIRECTORY_PATH, DEFAULT_FILE_NAME)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = self.DEFAULT_PATH

    def setUp(self) -> None:
        super().setUp()
        self.create_file()

    def tearDown(self) -> None:
        super().tearDown()
        self.delete_file()

    @staticmethod
    def create_file(path=DEFAULT_PATH) -> None:
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        open(path, "w").close()

    @classmethod
    def write_file_content(cls, content="", path=DEFAULT_PATH, mode="w+") -> None:
        if not os.path.exists(path):
            cls.create_file(path)
        with open(path, mode=mode, encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def delete_file(path=DEFAULT_PATH) -> None:
        if os.path.exists(os.path.dirname(path)):
            os.remove(path)

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
        self.write_file_content(content=content)
        self.instance.path = self.path
        self.instance.reflect()
        self.assertEqual(self.instance.contents[File.FILE_CONTENT_INDEX], content)


class EntriesDirectoryTest(EntryBaseTest):
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
        self.delete_directory()

    @staticmethod
    def create_directory(path=DEFAULT_PATH, sub_directory_names: tuple = DEFAULT_SUB_DIRECTORY_NAME) -> None:
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))

        EntriesDirectoryTest.create_sub_directory(path, sub_directory_names)

    @staticmethod
    def create_sub_directory(path=DEFAULT_PATH, sub_directory_names: tuple = DEFAULT_SUB_DIRECTORY_NAME) -> None:
        for name in sub_directory_names:
            if isinstance(name, str):
                if not os.path.exists(os.path.join(path, name)):
                    os.mkdir(os.path.join(path, name))
            else:
                EntriesDirectoryTest.create_sub_directory(path=path, sub_directory_names=sub_directory_names)

    @staticmethod
    def delete_directory(path=DEFAULT_PATH) -> None:
        if os.path.exists(path):
            sub_directory = os.listdir(path)
            for directory in sub_directory:
                shutil.rmtree(os.path.join(path, directory))

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
        self.create_sub_directory(sub_directory_names=sub_directory_names)
        self.instance.path = self.path
        self.instance.reflect()
        for name in sub_directory_names:
            if name not in self.instance.contents:
                self.fail()


if __name__ == '__main__':
    unittest.main()

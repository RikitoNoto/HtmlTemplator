import unittest
from unittest.mock import MagicMock
import shutil
import sys
import os
sys.path.append(os.path.abspath("../.."))

from src.dirTreeConfigurator.DirTreeConfigurator import DirTreeConfigurator

class DirTreeConfiguratorTest(unittest.TestCase):
    """
    the source directory path for test.
    this directory is created for each test.
    """
    SRC_DIR_PATH = os.path.abspath("../test_src")

    """
    the dest directory path for test.
    this directory is removed for each test.
    """
    DST_DIR_PATH = os.path.abspath("../test_dst")

    def setUp(self) -> None:
        os.mkdir(self.SRC_DIR_PATH) #create the source directory

    def tearDown(self) -> None:
        shutil.rmtree(self.SRC_DIR_PATH) # remove the source directory
        if(os.path.exists(self.DST_DIR_PATH)):
            # remove the dest directory if there is.
            shutil.rmtree(self.DST_DIR_PATH)

    def test_should_copy_tree_with_empty(self):
        DirTreeConfigurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))

    def test_should_copy_tree(self):
        dir_function_stub = self.add_file("test.html")

        DirTreeConfigurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        self.assertTrue(os.path.exists(dir_function_stub.spy_dst_file_path))

    def test_should_copy_tree_with_dir_function(self):
        dir_function_stub = self.add_file("test.html")

        DirTreeConfigurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, dir_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        self.assertTrue(os.path.exists(dir_function_stub.spy_dst_file_path))
        dir_function_stub.assert_called_with(self.DST_DIR_PATH)

    def test_should_copy_tree_with_file_function(self):
        dir_function_stub = self.add_file(name="test.html")

        DirTreeConfigurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, file_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        dir_function_stub.assert_called_with(dir_function_stub.spy_src_file_path)

    def test_should_copy_tree_with_file_content(self):
        dir_function_stub = self.add_file(name="test.html", content="test")

        DirTreeConfigurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, file_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        dir_function_stub.assert_called_with(dir_function_stub.spy_src_file_path)
        with open(dir_function_stub.spy_dst_file_path, "r") as file:
            self.assertEqual(file.read(), "test")

    def add_file(self, name: str, directory: str = "", content: str = "")->MagicMock:
        if(directory is not ""):
            src_file_path = os.path.join(self.SRC_DIR_PATH, directory, name)  # the source file path.
            dst_file_path = os.path.join(self.DST_DIR_PATH, directory, name)  # the destination file path.
        else:
            src_file_path = os.path.join(self.SRC_DIR_PATH, name)  # the source file path.
            dst_file_path = os.path.join(self.DST_DIR_PATH, name)  # the destination file path.

        dir_function_stub = MagicMock()

        # registe imfomations of file to the mock.
        dir_function_stub.spy_src_file_path = src_file_path
        dir_function_stub.spy_dst_file_path = dst_file_path
        dir_function_stub.spy_name = name
        dir_function_stub.spy_content = content

        dir_function_stub.return_value = DirTreeConfigurator.File(dst_file_path, content)

        open(src_file_path, mode="w").close()
        return dir_function_stub


if __name__ == '__main__':
    unittest.main()

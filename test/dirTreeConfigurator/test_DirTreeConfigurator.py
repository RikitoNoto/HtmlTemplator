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

    def test_should_create_the_instance(self):
        try:
            DirTreeConfigurator()
        except:
            self.fail("could not create instance.")

    def test_should_copy_tree_with_empty(self):
        dir_tree_configurator = DirTreeConfigurator()
        dir_tree_configurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))

    def test_should_copy_tree(self):
        dir_tree_configurator = DirTreeConfigurator()
        html_file_name = "test.html"
        open(os.path.join(self.SRC_DIR_PATH, html_file_name), mode="w").close()
        dir_tree_configurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        self.assertTrue(os.path.exists(os.path.join(self.DST_DIR_PATH, html_file_name)))

    def test_should_copy_tree_with_dir_function(self):
        dir_tree_configurator = DirTreeConfigurator()
        dir_function_stub = MagicMock()
        html_file_name = "test.html"
        open(os.path.join(self.SRC_DIR_PATH, html_file_name), mode="w").close()
        dir_tree_configurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, dir_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        self.assertTrue(os.path.exists(os.path.join(self.DST_DIR_PATH, html_file_name)))
        dir_function_stub.assert_called_with(self.DST_DIR_PATH)

    def test_should_copy_tree_with_file_function(self):
        dir_tree_configurator = DirTreeConfigurator()
        dir_function_stub = MagicMock()
        dir_function_stub.return_value = DirTreeConfigurator.File()
        html_file_name = "test.html"
        open(os.path.join(self.SRC_DIR_PATH, html_file_name), mode="w").close()
        dir_tree_configurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, file_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        dir_function_stub.assert_called_with(os.path.join(self.SRC_DIR_PATH, html_file_name))

    def test_should_copy_tree_with_file_content(self):
        dir_tree_configurator = DirTreeConfigurator()
        dir_function_stub = MagicMock()
        html_file_name = "test.html"
        path = os.path.join(self.SRC_DIR_PATH, html_file_name)

        dir_function_stub.return_value = DirTreeConfigurator.File(path, "test")

        open(path, mode="w").close()
        dir_tree_configurator.compile(self.SRC_DIR_PATH, self.DST_DIR_PATH, file_function=dir_function_stub)
        self.assertTrue(os.path.exists(self.DST_DIR_PATH))
        dir_function_stub.assert_called_with(os.path.join(self.SRC_DIR_PATH, html_file_name))
        with open(path, "r") as file:
            self.assertEqual(file.read(), "test")

if __name__ == '__main__':
    unittest.main()

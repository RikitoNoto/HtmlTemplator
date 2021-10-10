import unittest
import os
import sys
sys.path.append(os.path.abspath("../.."))

from src.Entry.Entry import EntryIF
from src.Entry.Entry import EntryBase


class EntryBaseTest(unittest.TestCase):
    class EntryBaseTemp(EntryBase):
        def reflect(self, *args, **kwargs) -> bool:
            return True

    INSTANCE_CLASS = EntryBaseTemp

    def setUp(self) -> None:
        self.instance = self.create_instance()

    def tearDown(self) -> None:
        del self.instance

    def create_instance(self) -> EntryIF:
        instance = self.INSTANCE_CLASS()
        instance.contents = self.INSTANCE_CLASS.DEFAULT_CONTENTS
        instance.path = self.INSTANCE_CLASS.DEFAULT_PATH
        instance.name = self.INSTANCE_CLASS.DEFAULT_NAME
        return instance

    def test_should_be_set_name(self):
        try:
            self.instance.name = "name"
        except:
            self.fail("could not set data.")

    def test_should_be_get_name(self):
        self.assertEqual(self.instance.name, "")

    def test_should_be_get_set_name(self):
        name = "name"
        self.instance.name = name
        self.assertEqual(self.instance.name, name)

    def test_should_be_set_path(self):
        try:
            self.instance.path = "path"
        except:
            self.fail("could not set data.")

    def test_should_be_get_path(self):
        self.assertEqual(self.instance.path, "")

    def test_should_be_get_set_path(self):
        path = "path"
        self.instance.path = path
        self.assertEqual(self.instance.path, path)

    def test_should_be_set_contents(self):
        try:
            self.instance.contents = []
        except:
            self.fail("could not set data.")

    def test_should_be_get_contents(self):
        self.assertEqual(self.instance.contents, [])

    def test_should_be_get_set_contents(self):
        contents = []
        self.instance.contents = contents
        self.assertEqual(self.instance.contents, contents)

    def test_should_be_get_content(self):
        contents = [1, 2, 3]
        self.instance.contents = contents

        for i in range(len(contents)):
            if self.instance.get_content(i) is not contents[i]:
                self.fail()

    def test_should_be_get_None_over_index(self):
        self.instance.contents = [1, 2, 3]
        self.assertEqual(self.instance.get_content(3), None)

    def test_should_be_set_content(self):
        self.instance.contents = [1, 2, 3]
        self.instance.set_content(1, 99)
        self.assertEqual(self.instance.contents[1], 99)

    def test_should_be_set_correct_contet_when_set_content_over_index(self):
        self.instance.set_content(3, 99)
        self.assertEqual(self.instance.contents[3], 99)

    def test_should_be_set_None_other_when_set_content_over_index(self):
        self.instance.set_content(3, 99)
        self.assertEqual(self.instance.contents[1], None)

    def test_should_be_append_content(self):
        self.instance.append_content(99)
        self.assertEqual(self.instance.contents[0], 99)

    def test_should_be_correct_len_del_content(self):
        self.instance.contents = [1, 2, 3, 4, 5]
        self.instance.del_content(2)
        self.assertEqual(len(self.instance.contents), 4)

    def test_should_be_correct_content_del_content(self):
        self.instance.contents = [1, 2, 3, 4, 5]
        self.instance.del_content(2)
        self.assertEqual(self.instance.contents[2], 4)


if __name__ == '__main__':
    unittest.main()

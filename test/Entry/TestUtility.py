import unittest
import os
import shutil


class TestUtility(unittest.TestCase):
    FILE_ENCODING = "utf-8"

    @staticmethod
    def create_file(path: str, content: str) -> bool:
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))

        if not os.path.exists(path):
            with open(path, mode="w", encoding=TestUtility.FILE_ENCODING) as file:
                file.write(content)
                file.close()
            return True
        return False

    @staticmethod
    def write_file_content(path: str, content: str, add=True) -> bool:
        if not os.path.exists(path):
            return TestUtility.create_file(path, content)
        else:
            mode: str = "w"
            if add:
                mode += "+"

            with open(path, mode=mode, encoding=TestUtility.FILE_ENCODING) as file:
                file.write(content)
                file.close()

            return True

    @staticmethod
    def delete_file(path: str) -> None:
        if os.path.exists(os.path.dirname(path)):
            os.remove(path)

    @staticmethod
    def create_directory(path: str, sub_directory_names: tuple) -> None:
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))

        TestUtility.create_sub_directory(path, sub_directory_names)

    @staticmethod
    def create_sub_directory(path: str, sub_directory_names: tuple) -> None:
        for name in sub_directory_names:
            if isinstance(name, str):
                if not os.path.exists(os.path.join(path, name)):
                    os.mkdir(os.path.join(path, name))
            else:
                TestUtility.create_sub_directory(path, sub_directory_names)

    @staticmethod
    def delete_directory(path: str) -> None:
        if os.path.exists(path):
            sub_directory = os.listdir(path)
            for directory in sub_directory:
                shutil.rmtree(os.path.join(path, directory))


if __name__ == '__main__':
    unittest.main()

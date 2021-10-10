__all__ = ["EntryIF", "EntryBase", "File", "Directory", "Link", "Device"]

from abc import ABCMeta
from abc import abstractmethod
from typing import Sequence
from typing import List
from typing import Any
import os


class EntryIF(metaclass=ABCMeta):

    @abstractmethod
    def reflect(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def del_name(self) -> None:
        pass

    @abstractmethod
    def get_contents(self) -> List:
        pass

    @abstractmethod
    def set_contents(self, content: Sequence) -> None:
        pass

    @abstractmethod
    def del_contents(self) -> None:
        pass

    @abstractmethod
    def get_path(self) -> str:
        pass

    @abstractmethod
    def set_path(self, path: str) -> None:
        pass

    @abstractmethod
    def del_path(self) -> None:
        pass

    @abstractmethod
    def get_content(self, index: int) -> Any:
        pass

    @abstractmethod
    def set_content(self, index: int, content: Any) -> None:
        pass

    @abstractmethod
    def del_content(self, index: int) -> bool:
        pass

    @abstractmethod
    def append_content(self, content: Any) -> None:
        pass

    name: str = property(get_name, set_name, del_name, "The name of the entry.")
    contents: List = property(get_contents, set_contents, del_contents, "The contents of the entry.")
    path: str = property(get_path, set_path, del_path, "The path of the entry.")


class EntryBase(EntryIF, metaclass=ABCMeta):
    DEFAULT_NAME: str = ""
    DEFAULT_CONTENTS: list = []
    DEFAULT_CONTENT: Any = None
    DEFAULT_PATH: str = ""

    def __init__(self, *args, **kwargs):
        self._name: str = self.DEFAULT_NAME
        self._content: list = self.DEFAULT_CONTENTS
        self._path: str = self.DEFAULT_PATH

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name: str = str(name)

    def del_name(self) -> None:
        del self._name

    def get_contents(self) -> List:
        return self._content

    def set_contents(self, content: Sequence) -> None:
        self._content: list = list(content)

    def del_contents(self) -> None:
        del self._content

    def get_path(self) -> str:
        return self._path

    def set_path(self, path: str) -> None:
        self._path: str = str(path)

    def del_path(self) -> None:
        del self._path

    def get_content(self, index: int) -> Any:
        if len(self._content) > index:
            return self._content[index]
        return None

    def set_content(self, index: int, content: Any) -> None:
        if len(self._content) <= index:
            for i in range(index - len(self._content) + 1):
                self.append_content(self.DEFAULT_CONTENT)

        self._content[index] = content

    def del_content(self, index: int) -> bool:
        if len(self._content) > index:
            del self._content[index]
            return True
        return False

    def append_content(self, content: Any) -> None:
        self._content.append(content)

    name: str = property(get_name, set_name, del_name, "The name of the entry.")
    contents: List = property(get_contents, set_contents, del_contents, "The contents of the entry.")
    path: str = property(get_path, set_path, del_path, "The path of the entry.")


class File(EntryBase):
    FILE_CONTENT_INDEX = 0
    FILE_ENCODING = "utf-8"

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def reflect(self, *args, **kwargs) -> bool:
        if (self.path != self.DEFAULT_PATH) or (self.path != ""):
            self._reflect_name(self.path)
            self._reflect_content(self.path)
            return True
        return False

    def _reflect_name(self, path: str) -> None:
        self._name = os.path.basename(path)

    def _reflect_content(self, path: str):
        with open(path, mode="r", encoding=self.FILE_ENCODING) as file:
            if len(self._content) > self.FILE_CONTENT_INDEX:
                self._content[self.FILE_CONTENT_INDEX] = file.read()
            else:
                self.append_content(file.read())


class Directory(EntryBase):

    def reflect(self, *args, **kwargs) -> bool:
        if (self.path != self.DEFAULT_PATH) or (self.path != ""):
            self._reflect_name(self.path)
            self._reflect_sub_directories(self.path)
            return True
        return False

    def _reflect_name(self, path: str) -> None:
        self.name = os.path.basename(path)

    def _reflect_sub_directories(self, path: str) -> None:
        self.contents = []
        for name in os.listdir(path):
            self.append_content(name)

class Link(EntryBase):
    pass


class Device(EntryBase):
    pass

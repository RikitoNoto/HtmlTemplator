from abc import ABCMeta
from abc import abstractmethod
from typing import List
from typing import Any

class Entry_if(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self)->str:
        pass

    @abstractmethod
    def set_name(self, name: str)->None:
        pass
    
    @abstractmethod
    def del_name(self)->None:
        pass

    @abstractmethod
    def get_contents(self) -> List:
        pass

    @abstractmethod
    def set_contents(self, content: List) -> None:
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
    def get_content(self, index: int)->Any:
        pass

    @abstractmethod
    def set_content(self, index: int, content: Any)->None:
        pass

    @abstractmethod
    def del_content(self, index: int)->bool:
        pass

    @abstractmethod
    def append_content(self, content: Any)->None:
        pass

    name: str = property(get_name, set_name, del_name, "The name of the entry.")
    contents: List = property(get_contents, set_contents, del_contents, "The contents of the entry.")
    path: str = property(get_path, set_path, del_path, "The path of the entry.")
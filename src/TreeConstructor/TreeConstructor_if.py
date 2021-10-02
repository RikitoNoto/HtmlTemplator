from abc import ABCMeta
from abc import abstractmethod
import sys
import os
sys.path.append(os.path.abspath(".."))

from src.EntryCompiler.EntryFactory_if import EntryFactory_if

class TreeConstructor_if(metaclass=ABCMeta):

    @abstractmethod
    def compile(self, src_path, dst_path)->bool:
        pass

    @abstractmethod
    def compile_directory(self, src_path, dst_path)->bool:
        pass

    @abstractmethod
    def compile_file(self, src_path, dst_path)->bool:
        pass
    
    @abstractmethod
    def get_file_factory(self)->EntryFactory_if:
        pass
    
    @abstractmethod
    def set_file_factory(self, file_factory: EntryFactory_if)->None:
        pass
    
    @abstractmethod
    def del_file_factory(self)->None:
        pass

    @abstractmethod
    def get_directory_factory(self) -> EntryFactory_if:
        pass

    @abstractmethod
    def set_directory_factory(self, directory_factory: EntryFactory_if) -> None:
        pass

    @abstractmethod
    def del_directory_factory(self) -> None:
        pass

    @abstractmethod
    def get_link_factory(self) -> EntryFactory_if:
        pass

    @abstractmethod
    def set_link_factory(self, link_factory: EntryFactory_if) -> None:
        pass

    @abstractmethod
    def del_link_factory(self) -> None:
        pass

    @abstractmethod
    def get_device_factory(self) -> EntryFactory_if:
        pass

    @abstractmethod
    def set_device_factory(self, device_factory: EntryFactory_if) -> None:
        pass

    @abstractmethod
    def del_device_factory(self) -> None:
        pass

    file_factory: EntryFactory_if = property(get_file_factory, set_file_factory, del_file_factory, "")
    directory_factory: EntryFactory_if = property(get_directory_factory, set_directory_factory, del_directory_factory, "")
    link_factory: EntryFactory_if = property(get_link_factory, set_link_factory, del_link_factory, "")
    device_factory: EntryFactory_if = property(get_device_factory, set_device_factory, del_device_factory, "")
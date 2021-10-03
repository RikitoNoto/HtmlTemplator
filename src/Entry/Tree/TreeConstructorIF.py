from abc import ABCMeta
from abc import abstractmethod
from typing import Union
import sys
import os
sys.path.append(os.path.abspath(".."))

try:
    from src.EntryCompiler.EntryCompilerIF import EntryCompilerIF as EntryCompiler
    from src.EntryCompiler.EntryIF import EntryIF
except ModuleNotFoundError:
    pass


class TreeConstructorIF(metaclass=ABCMeta):

    @abstractmethod
    def compile(self, src_path, dst_path) -> bool:
        pass

    @abstractmethod
    def compile_directory(self, src_path, dst_path) -> EntryIF:
        pass

    @abstractmethod
    def compile_file(self, src_path, dst_path) -> EntryIF:
        pass

    @abstractmethod
    def compile_link(self, src_path, dst_path) -> EntryIF:
        pass

    @abstractmethod
    def compile_device(self, src_path, dst_path) -> EntryIF:
        pass
    
    @abstractmethod
    def get_file_compiler(self) -> Union[EntryCompiler, None]:
        pass
    
    @abstractmethod
    def set_file_compiler(self, file_compiler: Union[EntryCompiler, None]) -> None:
        pass
    
    @abstractmethod
    def del_file_compiler(self) -> None:
        pass

    @abstractmethod
    def get_directory_compiler(self) -> Union[EntryCompiler, None]:
        pass

    @abstractmethod
    def set_directory_compiler(self, directory_compiler: Union[EntryCompiler, None]) -> None:
        pass

    @abstractmethod
    def del_directory_compiler(self) -> None:
        pass

    @abstractmethod
    def get_link_compiler(self) -> Union[EntryCompiler, None]:
        pass

    @abstractmethod
    def set_link_compiler(self, link_compiler: Union[EntryCompiler, None]) -> None:
        pass

    @abstractmethod
    def del_link_compiler(self) -> None:
        pass

    @abstractmethod
    def get_device_compiler(self) -> Union[EntryCompiler, None]:
        pass

    @abstractmethod
    def set_device_compiler(self, device_compiler: Union[EntryCompiler, None]) -> None:
        pass

    @abstractmethod
    def del_device_compiler(self) -> None:
        pass

    file_factory = property(get_file_compiler, set_file_compiler, del_file_compiler, "")
    directory_compiler = property(get_directory_compiler, set_directory_compiler, del_directory_compiler, "")
    link_compiler = property(get_link_compiler, set_link_compiler, del_link_compiler, "")
    device_compiler = property(get_device_compiler, set_device_compiler, del_device_compiler, "")

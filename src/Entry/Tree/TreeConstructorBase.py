from abc import abstractmethod
from typing import Union
import sys
import os
sys.path.append(os.path.abspath(".."))

try:
    from TreeConstructorIF import TreeConstructorIF
    from Compiler.EntryCompilerIF import EntryCompilerIF as EntryCompiler
    from Entry.EntryIF import EntryIF
except ModuleNotFoundError:
    from .TreeConstructorIF import TreeConstructorIF


class TreeConstructorBase(TreeConstructorIF):

    def __init__(self, *args, **kwargs):
        self._file_compiler: Union[EntryCompiler, None] = None
        self._directory_compiler: Union[EntryCompiler, None] = None
        self._link_compiler: Union[EntryCompiler, None] = None
        self._device_compiler: Union[EntryCompiler, None] = None

    @abstractmethod
    def compile(self, src_path, dst_path) -> bool:
        pass

    def compile_directory(self, src_path, dst_path) -> Union[EntryIF, None]:
        if self._directory_compiler is not None:
            return self._directory_compiler.create_entry(src_path, dst_path)
        return None

    def compile_file(self, src_path, dst_path) -> Union[EntryIF, None]:
        if self._file_compiler is not None:
            return self._file_compiler.create_entry(src_path, dst_path)
        return None

    def compile_link(self, src_path, dst_path) -> Union[EntryIF, None]:
        if self._link_compiler is not None:
            return self._link_compiler.create_entry(src_path, dst_path)
        return None

    def compile_device(self, src_path, dst_path) -> Union[EntryIF, None]:
        if self._device_compiler is not None:
            return self._device_compiler.create_entry(src_path, dst_path)
        return None

    def get_file_compiler(self) -> Union[EntryCompiler, None]:
        return self._file_compiler

    def set_file_compiler(self, file_compiler: Union[EntryCompiler, None]) -> None:
        if isinstance(file_compiler, EntryCompiler):
            self._file_compiler: EntryCompiler = file_compiler

    def del_file_compiler(self) -> None:
        del self._file_compiler

    def get_directory_compiler(self) -> Union[EntryCompiler, None]:
        return self._directory_compiler

    def set_directory_compiler(self, directory_compiler: Union[EntryCompiler, None]) -> None:
        if isinstance(directory_compiler, EntryCompiler):
            self._directory_compiler: EntryCompiler = directory_compiler

    def del_directory_compiler(self) -> None:
        del self._directory_compiler

    def get_link_compiler(self) -> Union[EntryCompiler, None]:
        return self._link_compiler

    def set_link_compiler(self, link_compiler: Union[EntryCompiler, None]) -> None:
        if isinstance(link_compiler, EntryCompiler):
            self._link_compiler: EntryCompiler = link_compiler

    def del_link_compiler(self) -> None:
        del self._link_compiler

    def get_device_compiler(self) -> Union[EntryCompiler, None]:
        return self._device_compiler

    def set_device_compiler(self, device_compiler: Union[EntryCompiler, None]) -> None:
        if isinstance(device_compiler, EntryCompiler):
            self._device_compiler: EntryCompiler = device_compiler

    def del_device_compiler(self) -> None:
        del self._device_compiler

    file_factory = property(get_file_compiler, set_file_compiler, del_file_compiler, "")
    directory_compiler = property(get_directory_compiler, set_directory_compiler, del_directory_compiler, "")
    link_compiler = property(get_link_compiler, set_link_compiler, del_link_compiler, "")
    device_compiler = property(get_device_compiler, set_device_compiler, del_device_compiler, "")

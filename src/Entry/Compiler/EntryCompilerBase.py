from abc import ABCMeta
from abc import abstractmethod
from typing import Callable
from typing import Union

try:
    from CompilerIF import CompilerIF
    from CompileDataIF import CompileDataIF
    from EntryCompilerIF import EntryCompilerIF
except ModuleNotFoundError:
    from .CompilerIF import CompilerIF
    from .CompileDataIF import CompileDataIF
    from .EntryCompilerIF import EntryCompilerIF


class EntryCompilerBase(EntryCompilerIF):

    def __init__(self, *args, **kwargs):
        self._name_compiler: Union[CompilerIF, None] = None
        self._content_compiler: Union[CompilerIF, None] = None
        self._data_factory_method: Union[Callable[[str, str], CompileDataIF], None] = None

    def get_name_compiler(self) -> Union[CompilerIF, None]:
        return self._name_compiler

    def set_name_compiler(self, compiler: Union[CompilerIF, None]) -> None:
        if isinstance(compiler, CompilerIF) or compiler is None:
            self._name_compiler: Union[CompilerIF, None] = compiler

    def del_name_compiler(self) -> None:
        self._name_compiler: Union[CompilerIF, None] = None

    def get_content_compiler(self) -> Union[CompilerIF, None]:
        return self._content_compiler

    def set_content_compiler(self, compiler: Union[CompilerIF, None]) -> None:
        if isinstance(compiler, CompilerIF) or compiler is None:
            self._content_compiler: Union[CompilerIF, None] = compiler

    def del_content_compiler(self) -> None:
        self._content_compiler: Union[CompilerIF, None] = None

    def get_data_factory_method(self) -> Union[Callable[[str, str], CompileDataIF], None]:
        return self._data_factory_method

    def set_data_factory_method(self, function: Union[Callable[[str, str], CompileDataIF], None]) -> None:
        if function is None or callable(function):
            self._data_factory_method: Union[Callable[[str, str], CompileDataIF], None] = function

    def del_data_factory_method(self) -> None:
        self._data_factory_method: Union[Callable[[str, str], CompileDataIF], None] = None

    name_compiler = property(get_name_compiler, set_name_compiler, del_name_compiler, "")
    content_compiler = property(get_content_compiler, set_content_compiler, del_content_compiler, "")
    data_factory_method = property(get_data_factory_method, set_data_factory_method, del_data_factory_method, "")
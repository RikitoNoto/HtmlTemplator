from abc import ABCMeta
from abc import abstractmethod
from typing import Callable
from typing import Union
try:
    from CompilerIF import CompilerIF
    from CompileDataIF import CompileDataIF
except ModuleNotFoundError:
    from .CompilerIF import CompilerIF
    from .CompileDataIF import CompileDataIF


class EntryCompilerIF(metaclass=ABCMeta):

    @abstractmethod
    def create_entry(self, src_dir_path: str, dst_dir_path: str, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_name_compiler(self) -> Union[CompilerIF, None]:
        pass
    
    @abstractmethod
    def set_name_compiler(self, compiler: Union[CompilerIF, None]) -> None:
        pass
    
    @abstractmethod
    def del_name_compiler(self) -> None:
        pass

    @abstractmethod
    def get_content_compiler(self) -> Union[CompilerIF, None]:
        pass
    
    @abstractmethod
    def set_content_compiler(self, compiler: Union[CompilerIF, None]) -> None:
        pass
    
    @abstractmethod
    def del_content_compiler(self) -> None:
        pass

    @abstractmethod
    def get_data_factory_method(self) -> Union[Callable[[str, str], CompileDataIF], None]:
        pass
    
    @abstractmethod
    def set_data_factory_method(self, compiler: Union[Callable[[str, str], CompileDataIF], None]) -> None:
        pass
    
    @abstractmethod
    def del_data_factory_method(self) -> None:
        pass

    name_compiler = property(get_name_compiler, set_name_compiler, del_name_compiler, "")
    content_compiler = property(get_content_compiler, set_content_compiler, del_content_compiler, "")
    data_factory_method = property(get_data_factory_method, set_data_factory_method, del_data_factory_method, "")

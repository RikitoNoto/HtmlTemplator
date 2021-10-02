from abc import ABCMeta
from abc import abstractmethod

class EntryFactory_if(metaclass=ABCMeta):

    @abstractmethod
    def create_entry(self, src_dir_path: str, dst_dir_path: str, *args, **kwargs):
        pass

    name_compiler = property()
    content_compiler = property()
    data_factory_method = property()
from abc import ABCMeta
from abc import abstractmethod

class ITemplator(metaclass=ABCMeta):
    
    def __init__(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def render(self, *args, **kwargs)->str:
        pass
    
    @abstractmethod
    def get_source(self)->str:
        pass
    
    @abstractmethod
    def set_source(self, source:str):
        pass
    
    @abstractmethod
    def del_source(self):
        pass

    @abstractmethod
    def get_data(self, index:str)->str:
        pass

    @abstractmethod
    def set_data(self, index:str, data:str)->None:
        pass

    @abstractmethod
    def del_data(self, index:str)->None:
        pass

    @abstractmethod
    def get_datas(self)->dict:
        pass
    
    @abstractmethod
    def set_datas(self, datas:dict):
        pass
    
    @abstractmethod
    def del_datas(self):
        pass
    
    source = property(get_source, set_source, del_source, "The source before compile.")
    datas = property(get_datas, set_datas, del_datas, "The datas or argments for compile.")
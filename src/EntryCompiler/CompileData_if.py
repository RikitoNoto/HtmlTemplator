from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod

class CompileData_if(metaclass=ABCMeta):

    @abstractmethod
    @classmethod
    def create_instance(cls, src_path: str, dst_path: str)->CompileData_if:
        pass
from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
from typing import Union


class CompileDataIF(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def create_instance(cls, src_path: str, dst_path: str) -> Union[CompileDataIF, None]:
        pass

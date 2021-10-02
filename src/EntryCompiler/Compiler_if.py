from abc import ABCMeta
from abc import abstractmethod
from typing import Tuple

class Compiler_if(metaclass=ABCMeta):

    @abstractmethod
    def compile(self, source: Tuple[str, ...])->str:
        pass
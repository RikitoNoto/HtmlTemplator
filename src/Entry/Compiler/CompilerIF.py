from abc import ABCMeta
from abc import abstractmethod
from typing import Tuple


class CompilerIF(metaclass=ABCMeta):

    @abstractmethod
    def compile(self, source: Tuple[str, ...]) -> Tuple[str, ...]:
        pass

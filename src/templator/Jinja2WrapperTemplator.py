from jinja2 import Template as Templator
from enum import IntEnum
from enum import auto

try:
    from BaseTemplator import BaseTemplator
except ModuleNotFoundError:
    from .BaseTemplator import BaseTemplator

class Jinja2WrapperTemplator(BaseTemplator):
    class __Args(IntEnum):
        SOURCE_INDEX_IN_ARGS = 0
        ARGC = auto()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if(len(args) < self.__Args.ARGC):
            raise self.ArgmentError("less args.")
        elif(isinstance(args[self.__Args.SOURCE_INDEX_IN_ARGS], str)):
            self.source = args[self.__Args.SOURCE_INDEX_IN_ARGS]


    def render(self, *args, **kwargs):
        return Templator(self.source).render(self.datas)
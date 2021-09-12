from abc import ABCMeta
from abc import abstractmethod

class ITemplatorLibraryAdapter(metaclass=ABCMeta):

    def __init__(self, templator_library_wrapper:type, *args, **kwargs):
        pass
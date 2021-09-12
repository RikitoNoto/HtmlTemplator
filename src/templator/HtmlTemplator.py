try:
    from BaseTemplator import BaseTemplator
    from ITemplatorLibraryAdapter import ITemplatorLibraryAdapter
except ModuleNotFoundError:
    from .BaseTemplator import BaseTemplator
    from .ITemplatorLibraryAdapter import ITemplatorLibraryAdapter

class HtmlTemplator(ITemplatorLibraryAdapter, BaseTemplator):
    
    def __init__(self, templator_library_wrapper:type, *args, **kwargs):
        super(ITemplatorLibraryAdapter, self).__init__(templator_library_wrapper, args, kwargs)
        super(BaseTemplator, self).__init__(args, kwargs)
        self.__initialize_args(templator_library_wrapper, args, kwargs)

    def render(self, *args, **kwargs)->str:
        return self.__render(datas=kwargs.get("datas"))

    def __render(self, datas:dict=None)->str:
        if(not datas):
            datas = {}
        return self.__templator_class(self.__source).render(datas)

    def __initialize_args(self, templator_library_wrapper:type, *args, **kwargs)->None:
        self.__templator_class = templator_library_wrapper
        self.__datas = dict()
        self.__source = ""

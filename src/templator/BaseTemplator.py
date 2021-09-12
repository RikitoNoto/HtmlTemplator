try:
    from ITemplator import ITemplator
except ModuleNotFoundError:
    from .ITemplator import ITemplator

class BaseTemplator(ITemplator):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        self._initialize_args(args, kwargs)

    def get_source(self)->str:
        return self._source

    def set_source(self, source:str):
        if(source is None):
            source = ""
        self._source = str(source)

    def del_source(self):
        self._source = ""

    def get_data(self, index: str) -> str:
        data = self._datas.get(index)
        if(data):
            return data
        else:
            return ""

    def set_data(self, index: str, data: str) -> None:
        self._datas[index] = data

    def del_data(self, index: str) -> None:
        data = self._datas.get(index)
        if(data):
            self._datas[index] = ""

    def get_datas(self) -> dict:
        return self._datas

    def set_datas(self, datas: dict):
        if(isinstance(datas, dict)):
            self._datas = datas
        else:
            raise self.ArgmentError("invalid args for datas.")

    def del_datas(self):
        self._datas = dict()

    def _initialize_args(self, *args, **kwargs)->None:
        self._datas = dict()
        self._source = ""

    source = property(get_source, set_source, del_source, "The source before compile.")
    datas = property(get_datas, set_datas, del_datas, "The datas or argments for compile.")

    class ArgmentError(Exception):
        """

        """
        pass
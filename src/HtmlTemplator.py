from jinja2 import Template

class HtmlTemplator:
    def __init__(self, text):
        self.__text = text

    def compile(self, *args, **kwargs)->str:
        return self.__compile(datas=kwargs.get("datas"))

    def __compile(self, datas:dict=None)->str:
        if(not datas):
            datas = {}
        return Template(self.__text).render(datas)

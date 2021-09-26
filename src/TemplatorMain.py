import re
import os
from typing import Callable

try:
    from dirTreeConfigurator.DirTreeConfigurator import DirTreeConfigurator
    from templator.HtmlTemplator import HtmlTemplator as Templator
    from templator.Jinja2WrapperTemplator import Jinja2WrapperTemplator as TemplatorLibrary
    from templator.ITemplator import ITemplator
    from templator.ITemplatorLibraryAdapter import ITemplatorLibraryAdapter
except ModuleNotFoundError:
    from .dirTreeConfigurator.DirTreeConfigurator import DirTreeConfigurator
    from .templator.HtmlTemplator import HtmlTemplator as Templator
    from .templator.Jinja2WrapperTemplator import Jinja2WrapperTemplator as TemplatorLibrary
    from .templator.ITemplator import ITemplator
    from .templator.ITemplatorLibraryAdapter import ITemplatorLibraryAdapter

DIRECTORY_READ_SKIP_PREFIX = ("_",)
DIRECTORY_READ_SKIP_SUFFIX = tuple()
DIRECTORY_READ_SKIP_STRING = tuple()

FILE_READ_SKIP_PREFIX = ("_",)
FILE_READ_SKIP_SUFFIX = tuple()
FILE_READ_SKIP_STRING = tuple()

def get_templator_library()->type:
    return TemplatorLibrary

def get_templator()->type:
    return Templator

def get_templator_instance()->ITemplatorLibraryAdapter:
    return get_templator()(get_templator_library())

def get_file_datas(source_file_path: str)->dict:
    #UNDONE
    return dict()

def is_name_skip(name: str, pattern: str)->bool:
    if(pattern is not ""):
        re_object = re.compile(pattern)
        result = re_object.search(name)
        if(result is not None):
            return True
    return False


def is_name_skip_with_prefix(name: str, prefix: str)->bool:
    if(prefix is not ""):
        return is_name_skip(name, "^{}".format(prefix))
    return False


def is_name_skip_with_suffix(name: str, suffix: str)->bool:
    if(suffix is not ""):
        return is_name_skip(name, "{}$".format(suffix))
    return False


def is_skip_with_contexts(name: str, contexts: tuple, check_func: Callable[[str, str], bool])->bool:
    result = False
    for context in contexts:
        if check_func(name, context):
            result = True
            break
    else:
        result = False
    return result


def is_file_read_skip(path: str)->bool:
    base_name = os.path.basename(path)
    is_skip = False
    if is_skip_with_contexts(base_name, FILE_READ_SKIP_PREFIX, is_name_skip_with_prefix):
        is_skip = True
    elif is_skip_with_contexts(base_name, FILE_READ_SKIP_SUFFIX, is_name_skip_with_suffix):
        is_skip = True
    elif is_skip_with_contexts(base_name, FILE_READ_SKIP_STRING, is_name_skip):
        is_skip = True

    return is_skip


def is_directory_read_skip(path: str)->bool:
    base_name = os.path.basename(path)
    is_skip = False
    if is_skip_with_contexts(base_name, DIRECTORY_READ_SKIP_PREFIX, is_name_skip_with_prefix):
        is_skip = True
    elif is_skip_with_contexts(base_name, DIRECTORY_READ_SKIP_SUFFIX, is_name_skip_with_suffix):
        is_skip = True
    elif is_skip_with_contexts(base_name, DIRECTORY_READ_SKIP_STRING, is_name_skip):
        is_skip = True

    return is_skip

def file_compile(file_path: str)->DirTreeConfigurator.File:
    templator = Templator(TemplatorLibrary)
    templator.source = file_path
    templator.datas = get_file_datas(file_path)



def dir_function_main(directory_path: str)->DirTreeConfigurator.Directory:
    pass


def file_function_main(file_path: str)->DirTreeConfigurator.File:
    file = DirTreeConfigurator.File()
    if(not is_file_read_skip(file_path)):
        pass



if __name__ == '__main__':
    import sys
    if(len(sys.argv) < 2):
        raise ValueError("Usage: python {} <source_path> <destination_path>".format(__file__))

    src_path = sys.argv[0]
    dst_path = sys.argv[1]

    DirTreeConfigurator.compile(src_path=src_path, dst_path=dst_path , dir_function=dir_function_main, file_function=file_function_main)
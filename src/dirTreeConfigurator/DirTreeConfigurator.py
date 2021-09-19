import os
import shutil
from typing import Callable
from typing import Union

class DirTreeConfigurator:
    class File:
        def __init__(self, path="", content=""):
            self.path = path
            self.content = content
            
        def get_path(self)->str:
            return self.__path
        
        def set_path(self, path)->None:
            self.__path = str(path)
            
        def del_path(self)->None:
            self.__path = ""
            
        def get_content(self) -> str:
            return self.__content

        def set_content(self, content) -> None:
            self.__content = str(content)

        def del_content(self) -> None:
            self.__content = ""

        path = property(get_path, set_path, del_path)
        content = property(get_content, set_content, del_content)

    @classmethod
    def compile(cls, src_path:str, dst_path:str, dir_function=None, file_function=None):
        # shutil.copytree(src=src_path, dst=dst_path)
        cls.__create_directory_tree(src_path, dst_path, dir_function, file_function)

    @classmethod
    def __create_directory_tree(cls, src_path:str, dst_path:str,
                                dir_function:Union[Callable[[str], str], None]=None,
                                file_function:Union[Callable[[str], File], None]=None):
        """
        create the directory tree based on src_path.
        :param: src_path: The path of the directory tree.(source)
        :param: dst_path: The path of the directory tree.(dest)
        :param: dir_function: The function to execute the directory.
                              This function is required take a file path as an argument and return a directory name.
        :param: file_function: The function to execute the file.
                               This function is required take a file path as an argument and return FileObject.
        :return: None
        """
        if(not os.path.exists(dst_path)):
            os.mkdir(dst_path)
            if(dir_function is not None):
                dir_function(dst_path)

        for name in os.listdir(src_path):
            if(os.path.isfile(os.path.join(src_path, name))):
                if(file_function is not None):
                    file = file_function(os.path.join(src_path, name))#TODO: this function's output.
                    if(file.path is not ""):
                        with open(file.path, mode="w") as f:
                            f.write(file.content)
                else:
                    shutil.copyfile(os.path.join(src_path, name), os.path.join(dst_path, name))

            elif(os.path.isdir(os.path.join(src_path, name))):
                dst_directory_name = os.path.join(dst_path, name)
                os.mkdir(dst_directory_name)
                if(dir_function is not None):
                    dir_function(dst_directory_name)
                cls.__create_directory_tree(os.path.join(src_path, name), dst_directory_name, dir_function=dir_function, file_function=file_function)

        
import os
import shutil
from typing import Callable
from typing import Union

class DirTreeConfigurator:
    class File:
        """
        A class that represents a file.
        """
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

        path = property(get_path, set_path, del_path, "the path of this file.")
        content = property(get_content, set_content, del_content, "the content of this file.")

    class Directory:
        """
        A class that represents a directory.
        """

        def __init__(self, is_read=True, path=""):
            self.path = path
            self.is_read = is_read

        def get_path(self) -> str:
            return self.__path

        def set_path(self, path) -> None:
            self.__path = str(path)

        def del_path(self) -> None:
            self.__path = ""

        def get_is_read(self) -> bool:
            return self.__is_read

        def set_is_read(self, is_read:bool) -> None:
            if(isinstance(is_read, bool)):
               self.__is_read = is_read

        def del_is_read(self) -> None:
            self.__is_read = True

        path = property(get_path, set_path, del_path, "the path of this file.")
        is_read = property(get_is_read, set_is_read, del_is_read, "there is need to read the directory.")

    @classmethod
    def compile(cls, src_path:str, dst_path:str, dir_function=None, file_function=None):
        cls.__create_directory_tree(src_path, dst_path, dir_function, file_function)

    @classmethod
    def __create_directory_tree(cls, src_path: str, dst_path: str,
                                dir_function: Union[Callable[[str], Directory], None]=None,
                                file_function: Union[Callable[[str], File], None]=None):
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

        """
        if there is not the directory of dest,
        then create the dest directory first.
        """
        if(not os.path.exists(dst_path)):  # if there is not the directory of dest
            os.mkdir(dst_path)
            if(dir_function is not None):
                dir_function(dst_path)

        # search the source directory.
        # if discover a directory, call this function recursively.
        for name in os.listdir(src_path):
            # source path(file or directory).
            src_target_path = os.path.join(src_path, name)

            # if the target is file.
            if(os.path.isfile(src_target_path)):
                if(file_function is not None):  # there is the file function.
                    file = file_function(src_target_path)
                    if(file.path is not ""):
                        with open(file.path, mode="w") as f:
                            f.write(file.content)

                else:  # if file function is None, then copy the file.
                    shutil.copyfile(src_target_path, os.path.join(dst_path, name))

            elif(os.path.isdir(src_target_path)):
                dst_directory_name = os.path.join(dst_path, name)

                # if there is the function of a directory, execute the function with the dest path as an argument.
                if(dir_function is not None):
                    directory_info = dir_function(dst_directory_name)
                    if(directory_info.is_read):
                        os.mkdir(directory_info.path)
                        cls.__create_directory_tree(src_target_path, directory_info.path, dir_function=dir_function, file_function=file_function)

                else:
                    os.mkdir(dst_directory_name)  # make the dest directory
                    cls.__create_directory_tree(src_target_path, dst_directory_name, dir_function=dir_function, file_function=file_function)

from pathlib import Path
import copy

from box.box import Box
from box.boxId import IdWrongLength, IdNotAlphabetic
from box.boxCollection import BoxCollection


class FileStorage:
    """
    Represent data access to file storage

    Methods
    -------
    register_into_box_collection -> set
        return a BoxCollection object filled with box ids provided in the file

    Properties
    ----------
    path -> Path
        return the path object associated with the actual file
    """
    
    def __init__(self, str_path:str) -> None:
        """
        Constructs all the necessary attributes for the FileStorage object.

        Parameters
        ----------
            str_path : str
                path to the file to read
        """
        self.__data_validation_path(str_path)
        path = Path(str_path)
        self.__validate_file_path(path)
        self.__path = path

    def __data_validation_path(self, path:str) -> None:
        """Validate the provided data, raise an error if not valid"""
        if type(path) is not str: raise TypeError('path must be a string')
    
    def __validate_file_path(self, path:Path) -> None:
        """Validate the provided path, raise an error if not valid"""
        if not path.exists(): raise PathNotExists(str(path))
        if not path.is_file(): raise NotAFile(str(path))

    def register_into_box_collection(self) -> tuple[BoxCollection, list[dict[str,str|IdNotAlphabetic|IdWrongLength]]]:
        """return a BoxCollection object filled with box ids provided in the file"""
        box_collection = BoxCollection()
        self.__validate_file_path(self.__path)

        box_collection = copy.copy(box_collection)
        unregistered_boxes: list[dict[str,str|IdNotAlphabetic|IdWrongLength]] = []

        for box_id in self.__path.open('rt'):
            if box_id[-1] == '\n': box_id = box_id[:-1] #delete newline char
            try:
                box = Box(box_id)
                box_collection.register(box)
            except (IdNotAlphabetic, IdWrongLength) as e:
                box_error = {'error':e,'box_id':box_id}
                unregistered_boxes.append(box_error)
        
        return box_collection, unregistered_boxes

    @property
    def path(self) -> Path:
        """return the path object associated with the actual file"""
        return self.__path


class PathNotExists(ValueError):
    def __init__(self, str_path: str):
        self.message = f'Path : {str_path}'
        super().__init__(self.message)

class NotAFile(ValueError):
    def __init__(self, str_path: str):
        self.message = f'Path : {str_path}'
        super().__init__(self.message)

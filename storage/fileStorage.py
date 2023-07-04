from pathlib import Path
import copy

from storage.storage import Storage
from box.box import Box
from box.boxId import IdWrongLength, IdNotAlphabetic
from box.boxCollection import BoxCollection


class FileStorage:
    
    def __init__(self, str_path:str) -> None:
        self.__data_validation_path(str_path)
        path = Path(str_path)
        self.__validate_file_path(path)
        self.__path = path

    def __data_validation_path(self, path:str) -> None:
        if type(path) is not str: raise TypeError('path must be a string')
    
    def __validate_file_path(self, path:Path) -> None:
        if not path.exists(): raise PathNotExists(str(path))
        if not path.is_file(): raise NotAFile(str(path))

    def __data_validation_box_collection(self, box_collection: BoxCollection) -> None:
        if type(box_collection) != BoxCollection: raise TypeError('box_collection must be a BoxCollection object')

    def register_into_box_collection(self, box_collection: BoxCollection) -> tuple[BoxCollection, list[dict[str,str|IdNotAlphabetic|IdWrongLength]]]:
        self.__data_validation_box_collection(box_collection)
        self.__validate_file_path(self.__path)

        box_collection = copy.copy(box_collection)
        unregistered_boxes: list[dict[str,str|IdNotAlphabetic|IdWrongLength]] = []

        for box_id in self.__path.open('rt'):
            box_id = box_id[:-1] #delete newline char
            try:
                box = Box(box_id)
                box_collection.register(box)
            except (IdNotAlphabetic, IdWrongLength) as e:
                box_error = {'error':e,'box_id':box_id}
                unregistered_boxes.append(box_error)
        
        return box_collection, unregistered_boxes


    @property
    def path(self) -> Path:
        return self.__path


class PathNotExists(ValueError):
    def __init__(self, str_path: str):
        self.message = f'Path : {str_path}'
        super().__init__(self.message)

class NotAFile(ValueError):
    def __init__(self, str_path: str):
        self.message = f'Path : {str_path}'
        super().__init__(self.message)

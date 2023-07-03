class BoxId:
    __id_len: int = 26

    @staticmethod
    def get_id_len() -> int:
        return BoxId.__id_len


    def __init__(self, id: str) -> None:
        self.__data_validation_id(id)
        self.__id = id

    def __data_validation_id(self, id: str) -> None:
        if type(id) is not str : raise TypeError('id must be a string')
        if len(id) != self.__id_len: raise IdWrongLength(f'length of id must be {self.__id_len}')
        if not id.isalpha(): raise IdNotAlphabetic('id must contain only alphabetic char')

    @property
    def id(self) -> str:
        return self.__id

    def __str__(self) -> str:
        return self.id


class IdWrongLength(ValueError):
    pass

class IdNotAlphabetic(ValueError):
    pass
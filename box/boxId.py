from __future__ import annotations #fix for return typehint warning at staticmethod get_random_box_id
import random
import string

class BoxId:
    """
    Represent a box id

    Static Methods
    -------
    get_id_len -> int
        return the required length for an id

    get_random_box_id -> BoxId
        return a valid random BoxId

    Properties
    ----------
    id -> int
        return the id
    """
    __id_len: int = 26

    @staticmethod
    def get_id_len() -> int:
        """return the required length for an id"""
        return BoxId.__id_len
    
    @staticmethod
    def get_random_box_id() -> BoxId:
       """return a valid random BoxId"""
       id = ''.join(random.choice(string.ascii_letters) for __ in range(BoxId.get_id_len()))
       return BoxId(id)


    def __init__(self, id: str) -> None:
        """
        Constructs all the necessary attributes for the BoxId object.

        Parameters
        ----------
            id : str
                id that is associated with the box
        """
        self.__data_validation_id(id)
        self.__id = id

    def __data_validation_id(self, id: str) -> None:
        """Validate the provided data, raise an error if not valid"""
        if type(id) is not str : raise TypeError('id must be a string')
        if len(id) != self.__id_len: raise IdWrongLength(f'length of id must be {self.__id_len}')
        if not id.isalpha(): raise IdNotAlphabetic('id must contain only alphabetic char')

    @property
    def id(self) -> str:
        """return the box id"""
        return self.__id

    def __str__(self) -> str:
        return self.id


class IdWrongLength(ValueError):
    pass

class IdNotAlphabetic(ValueError):
    pass
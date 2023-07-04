from box.box import Box
from utils import is_containing_exactly_x_number_of_any_char


class BoxCollection:
    """
    Represent a collection of boxes.
    
    Methods
    -------
    register -> None
        add a box to the collection
        raise BoxAlreadyExistInCollection if the box is already is the collection

    unregister -> None
        remove a box from the collection
        raise BoxNotExistInCollection if the box is not in the collection

    Properties
    ----------
    checksum -> int
        returns the checksum calculate with the boxes inside the collection

    collection -> set
        returns a copy the __collection attribute that contains all the boxes
    """


    def __init__(self) -> None:
        self.__collection: set = set()

    def __iter__(self):
        return self.__collection.__iter__()
    
    def __len__(self):
        return len(self.collection)

    def __data_validation_box(self, box: Box) -> None:
        """Validate the provided data, raise an error if not valid"""
        if type(box) != Box: raise TypeError('box must be a Box object')

    def register(self, box: Box) -> None:
        """add a box to the collection
        raise BoxAlreadyExistInCollection if the box is already is the collection"""
        self.__data_validation_box(box)
        if box in self.__collection: raise BoxAlreadyExistInCollection(box.id)
        self.__collection.add(box)

    def unregister(self, box: Box) -> None:
        """remove a box from the collection
        raise BoxNotExistInCollection if the box is not in the collection"""
        self.__data_validation_box(box)
        try: self.__collection.remove(box)
        except KeyError: raise BoxNotExistInCollection(box.id)

    @property
    def checksum(self) -> int:
        """returns the checksum calculate with the boxes inside the collection"""
        count_exactly_two_same_letter = 0
        count_exactly_three_same_letter = 0
        for box in self.__collection:
            id = box.id
            count_exactly_two_same_letter += int(is_containing_exactly_x_number_of_any_char(id, 2))
            count_exactly_three_same_letter += int(is_containing_exactly_x_number_of_any_char(id, 3))
        return count_exactly_two_same_letter * count_exactly_three_same_letter

    @property
    def collection(self) -> set:
        """returns a copy the set that contains all the boxes"""
        return self.__collection.copy()


class BoxNotExistInCollection(KeyError):
     def __init__(self, box_id: str):
        self.message = f'Box id : {box_id}'
        super().__init__(self.message)

class BoxAlreadyExistInCollection(KeyError):
     def __init__(self, box_id: str):
        self.message = f'Box id : {box_id}'
        super().__init__(self.message)
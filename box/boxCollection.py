from box.box import Box

class BoxCollection:
    def __init__(self) -> None:
        self.__collection: set = set()

    def __iter__(self):
        return self.__collection.__iter__()
    
    def __len__(self):
        return len(self.collection)

    def __data_validation_box(self, box: Box) -> None:
        if type(box) != Box: raise TypeError('box must be a Box object')

    def register(self, box: Box) -> None:
        self.__data_validation_box(box)
        if box in self.__collection: raise BoxAlreadyExistInCollection(box.id)
        self.__collection.add(box)

    def unregister(self, box: Box) -> None:
        self.__data_validation_box(box)
        try: self.__collection.remove(box)
        except KeyError: raise BoxNotExistInCollection(box.id)

    @property
    def collection(self) -> set:
        return self.__collection.copy()


class BoxNotExistInCollection(KeyError):
     def __init__(self, box_id: str):
        self.message = f'Box id : {box_id}'
        super().__init__(self.message)

class BoxAlreadyExistInCollection(KeyError):
     def __init__(self, box_id: str):
        self.message = f'Box id : {box_id}'
        super().__init__(self.message)
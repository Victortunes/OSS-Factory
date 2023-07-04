from box.boxId import BoxId

class Box:

    def __init__(self, id: str) -> None:
        self.__box_id = BoxId(id)

    @property
    def id(self) -> str:
        return self.__box_id.id
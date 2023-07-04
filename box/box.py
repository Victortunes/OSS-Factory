from box.boxId import BoxId

class Box:
    """
    A class that represent a box.
    
    Property
    --------
    id -> str
        return the id of the box
    """

    def __init__(self, id: str) -> None:
        """
        Constructs all the necessary attributes for the Box object.

        Parameters
        ----------
            id : str
                id that is associated with the box
        """
        self.__box_id = BoxId(id)

    @property
    def id(self) -> str:
        """
        Returns the box id
        
            Returns:
                id (str): id of the box
        """
        return self.__box_id.id
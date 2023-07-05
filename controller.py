from storage.fileStorage import FileStorage, NotAFile, PathNotExists
from box.boxCollection import BoxCollection
from display import Display
from utils import common_letters

class Controller:
    """
    A class that interface the screen and data

    Method
    ------
    run -> None
        response to the two questions of the test
    """


    def __init__(self, display: Display):
        if type(display) is not Display: raise TypeError('display must be a Display object')
        self.__display = display

    def run(self, path:str):
        """response to the two questions of the test"""
        if type(path) is not str: raise TypeError('path is not a string')
        try:
            file_storage = FileStorage(path)
            box_collection, unregistered_boxes = file_storage.register_into_box_collection()
        except (IOError, NotAFile, PathNotExists) as e:
            self.__display.error(str(e))
        else:
            if unregistered_boxes:
                warn_msg = ''
                warn_msg += 'Warning somes boxes hasn\'t be imported\n'
                for unregistered_box in unregistered_boxes:
                    warn_msg += f'Box id : {unregistered_box["box_id"]} Reason : {unregistered_box["error"]}\n'
                self.__display.warning(warn_msg)
            
            self.__answer_part1(box_collection)
            self.__answer_part2(box_collection)

    def __answer_part1(self, box_collection: BoxCollection):
        """response to the first question of the test"""
        if type(box_collection) is not BoxCollection: raise TypeError('box_collection must be a BoxCollection object')

        cheksum = box_collection.checksum

        self.__display.title('Part 1')
        self.__display.question_with_answer('🤔 What is the checksum value?', f'Cheksum : {cheksum}')
        self.__display.print(f'Total registered boxes : {len(box_collection)}')

    def __answer_part2(self, box_collection: BoxCollection):
        """response to the second question of the test"""
        if type(box_collection) is not BoxCollection: raise TypeError('box_collection must be a BoxCollection object')

        self.__display.title('Part 2')
        answer_msg = ''

        near_boxes_list = box_collection.get_near_box_ids()
        for near_boxes in near_boxes_list:
            box_id_a = near_boxes[0].id
            box_id_b = near_boxes[1].id
            similiraties = common_letters(box_id_a, box_id_b)
            answer_msg += f'Box id a/b : {box_id_a} / {box_id_b} -> {similiraties}\n'

        self.__display.question_with_answer('🤔 What letters are common between the two correct box IDs ?', answer_msg)


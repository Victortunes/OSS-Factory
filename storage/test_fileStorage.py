import unittest
import tempfile
from pathlib import Path
import os

from box.boxId import BoxId, IdWrongLength, IdNotAlphabetic
from box.box import Box
from box.boxCollection import BoxCollection
from storage.fileStorage import FileStorage, NotAFile, PathNotExists


class TestFileStoragePath(unittest.TestCase):

    def setUp(self) -> None:
        self.__str_path: str = './storage/input.txt'

    def test_path_valid(self):
        self.assertEqual(FileStorage(self.__str_path).path, Path(self.__str_path))

    def test_path_invalid_datatype(self):
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_path_not_exists(self):
        with self.assertRaises(PathNotExists):
            FileStorage(' ')
    
    def test_path_not_a_file(self):
        with self.assertRaises(NotAFile):
            FileStorage('./storage')


class TestFileStorageRegister(unittest.TestCase):

    def setUp(self) -> None:
        self.__file = tempfile.TemporaryFile('at', delete=False)
        self.__file_name = self.__file.name
        self.__expected_box_collection: set[Box] = set()
    
    def tearDown(self) -> None:
        os.remove(self.__file_name)

    def test_valid_import_file(self):
        for __ in range(10):
            box = Box(BoxId.get_random_box_id().id)
            self.__expected_box_collection.add(box)
            self.__file.write(f'{box.id}\n')
        
        self.__file.close()
        
        file_storage = FileStorage(self.__file_name)
        actual_box_collection, unregistered_boxes = file_storage.register_into_box_collection()

        self.assertEqual(len(unregistered_boxes), 0, "Error during importation of box ids")
        self.assertEqual(set(map(lambda box: box.id, actual_box_collection.collection)), set(map(lambda box: box.id, self.__expected_box_collection)), msg='Missing or more or incorrect imported box ids')

    def test_valid_import_file_without_new_line_at_the_end(self):
            repetition = 10
            for i in range(repetition):
                box = Box(BoxId.get_random_box_id().id)
                self.__expected_box_collection.add(box)
                self.__file.write(box.id)
                if i+1 != repetition: self.__file.write('\n')
            
            self.__file.close()
            
            file_storage = FileStorage(self.__file_name)
            actual_box_collection, unregistered_boxes = file_storage.register_into_box_collection()

            self.assertEqual(len(unregistered_boxes), 0, "Error during importation of box ids")
            self.assertEqual(set(map(lambda box: box.id, actual_box_collection.collection)), set(map(lambda box: box.id, self.__expected_box_collection)), msg='Missing or more or incorrect imported box ids')

    def test_invalid_import_file_with_invalid_length_box_id(self):
        invalid_box_id = 'abce'
        self.__file.write(f'{invalid_box_id}\n')        
        self.__file.close()
        
        file_storage = FileStorage(self.__file_name)
        actual_box_collection, unregistered_boxes = file_storage.register_into_box_collection()

        self.assertEqual(len(actual_box_collection), 0, msg="Valid if the invalid box isn't in the valid list") 
        self.assertEqual(len(unregistered_boxes), 1, msg='Valid if the invalid box id is in the invalid list')
        self.assertEqual(unregistered_boxes[0]['box_id'], invalid_box_id, msg='Check if the returned invalid box id is the same as expected')
        self.assertEqual(type(unregistered_boxes[0]['error']), IdWrongLength, msg='Check if the returned error is the same as expected')

    def test_invalid_import_file_with_invalid_non_alpha_box_id(self):
        invalid_box_id = 'a' + '1'*(BoxId.get_max_id_len()-1)
        self.__file.write(f'{invalid_box_id}\n')        
        self.__file.close()
        
        file_storage = FileStorage(self.__file_name)
        actual_box_collection, unregistered_boxes = file_storage.register_into_box_collection()

        self.assertEqual(len(actual_box_collection), 0, msg="Valid if the invalid box isn't in the valid list") 
        self.assertEqual(len(unregistered_boxes), 1, msg='Valid if the invalid box id is in the invalid list')
        self.assertEqual(unregistered_boxes[0]['box_id'], invalid_box_id, msg='Check if the returned invalid box id is the same as expected')
        self.assertEqual(type(unregistered_boxes[0]['error']), IdNotAlphabetic, msg='Check if the returned error is the same as expected')



if __name__ == '__main__':
    unittest.main()
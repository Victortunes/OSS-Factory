import unittest
import random

from box.boxCollection import BoxCollection, BoxAlreadyExistInCollection, BoxNotExistInCollection
from box.box import Box
from box.boxId import BoxId

class TestBoxCollectionEmpty(unittest.TestCase):

    def setUp(self):
        self.__box_collection = BoxCollection()

    def test_register_box(self):
        box_set = set()
        for __ in range(10):
            box = Box(BoxId.get_random_box_id().id)
            box_set.add(box) # ok
            try: self.__box_collection.register(box) #should fail, already added
            except BoxAlreadyExistInCollection: pass 

        self.assertEqual(box_set, self.__box_collection.collection)

    def test_register_box_wrong_datatype(self):
        with self.assertRaises(TypeError):
            self.__box_collection.register(1) # type: ignore

    def test_checksum_empty_collection(self):
        self.assertEqual(self.__box_collection.checksum, 0)
    
    def test_valid_checksum(self):
        expected = 12
        box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

        for box_id in box_ids:
            self.__box_collection.register(Box(box_id))
        
        self.assertEqual(expected, self.__box_collection.checksum)

    def test_valid_near_box_ids(self):
        expected = ('fghij','fguij')
        box_ids = ('abcde', 'fghij','klmno','pqrst','fguij','axcye','wvxyz')
        for box_id in box_ids:
            self.__box_collection.register(Box(box_id))
        near_boxes = self.__box_collection.get_near_box_ids()
        actual = (near_boxes[0][0].id, near_boxes[0][1].id)
        self.assertEqual(len(near_boxes), 1) #only one couple should be returned
        self.assertEqual(set(expected),set(actual))

    def test_inequal_length_id_near_box_ids(self):
        expected = ('fghij','fguij')
        box_ids = ('aegjutcsre','fguij','acbde', 'azertzdqy','fghij', 'dsqdezdgvh')
        for box_id in box_ids:
            self.__box_collection.register(Box(box_id))
        near_boxes = self.__box_collection.get_near_box_ids()
        actual = (near_boxes[0][0].id, near_boxes[0][1].id)
        self.assertEqual(len(near_boxes), 1) #only one couple should be returned
        self.assertEqual(set(expected), set(actual))

    def test_only_one_box_near_box_ids(self):
        self.__box_collection.register(Box(BoxId.get_random_box_id().id))
        near_boxes = self.__box_collection.get_near_box_ids()
        self.assertEqual(len(near_boxes), 0)


class TestBoxCollectionPrefilled(unittest.TestCase):

    def setUp(self):
        self.__number_prefilled_boxes = 10
        self.__box_collection = BoxCollection()
        self.__prefilled_boxes: set[Box] = set()
        for __ in range(self.__number_prefilled_boxes):
            box = Box(BoxId.get_random_box_id().id)
            self.__prefilled_boxes.add(box)
            try: self.__box_collection.register(box)
            except BoxAlreadyExistInCollection: pass 


    def test_for_loop(self):
        collected_box = set()
        for box in self.__box_collection:
            collected_box.add(box)
        self.assertEqual(collected_box,self.__prefilled_boxes)

    def test_no_side_effects(self):
        copied_collection = self.__box_collection.collection
        copied_collection.pop()
        unmodified_collection = self.__box_collection.collection
        self.assertNotEqual(copied_collection, unmodified_collection)

    def test_unregister_box(self):
        box_to_remove = self.__box_collection.collection.pop()
        self.__box_collection.unregister(box_to_remove) #ok
        with self.assertRaises(BoxNotExistInCollection):
            self.__box_collection.unregister(box_to_remove) #should fail, already deleted
    
    def test_unregister_box_wrong_datatype(self):
        with self.assertRaises(TypeError):
            self.__box_collection.unregister(1) # type: ignore

    def test_length_method(self):
        self.assertEqual(len(self.__box_collection), self.__number_prefilled_boxes)        



if __name__ == '__main__':
    unittest.main()
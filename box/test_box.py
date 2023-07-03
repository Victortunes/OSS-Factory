import unittest

from boxId import BoxId
from box import Box


class TestBox(unittest.TestCase):

    def setUp(self) -> None:
        self.__id_len: int = BoxId.get_id_len()

    def test_id_valid(self):
        id = 'a'*self.__id_len
        box = Box(id)
        self.assertEqual(id, box.id)

    def test_id_wrong_type(self):
        id = 1*10**(self.__id_len-1)
        with self.assertRaises(TypeError):
            Box(id)

if __name__ == '__main__':
    unittest.main()
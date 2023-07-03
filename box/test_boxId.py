import unittest

from boxId import BoxId, IdWrongLength, IdNotAlphabetic


class TestBoxId(unittest.TestCase):

    def setUp(self):
        self.__id_len: int = BoxId.get_id_len()

    def test_id_valid(self):
        id = 'a'*self.__id_len
        boxId = BoxId(id)
        self.assertEqual(id, boxId.id)

    def test_id_inferior_length(self):
        id = 'a'*(self.__id_len-1)
        with self.assertRaises(IdWrongLength):
            BoxId(id)

    def test_id_superior_length(self):
        id = 'a'*(self.__id_len+1)
        with self.assertRaises(IdWrongLength):
            BoxId(id)

    def test_id_with_number(self):
        id = '1'*self.__id_len
        with self.assertRaises(IdNotAlphabetic):
            BoxId(id)
    
    def test_id_with_alpha_and_number(self):
        len_a = self.__id_len//2
        len_b = len_a + self.__id_len%2
        id = 'a'*len_a + '1'*len_b
        with self.assertRaises(IdNotAlphabetic):
            BoxId(id)


if __name__ == '__main__':
    unittest.main()
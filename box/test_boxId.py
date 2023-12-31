import unittest

from box.boxId import BoxId, IdWrongLength, IdNotAlphabetic


class TestBoxId(unittest.TestCase):

    def setUp(self):
        self.__max_id_len: int = BoxId.get_max_id_len()
        self.__min_id_len: int = BoxId.get_min_id_len()

    def test_id_valid(self):
        id = 'a'*self.__max_id_len
        boxId = BoxId(id)
        self.assertEqual(id, boxId.id)

    def test_id_inferior_length(self):
        id = 'a'*(self.__min_id_len-1)
        with self.assertRaises(IdWrongLength):
            BoxId(id)

    def test_id_superior_length(self):
        id = 'a'*(self.__max_id_len+1)
        with self.assertRaises(IdWrongLength):
            BoxId(id)

    def test_id_with_number(self):
        id = '1'*self.__max_id_len
        with self.assertRaises(IdNotAlphabetic):
            BoxId(id)
    
    def test_id_with_alpha_and_number(self):
        len_a = self.__max_id_len//2
        len_b = len_a + self.__max_id_len%2
        id = 'a'*len_a + '1'*len_b
        with self.assertRaises(IdNotAlphabetic):
            BoxId(id)

    def test_id_wrong_type(self):
        id = 1*10**(self.__max_id_len-1)
        with self.assertRaises(TypeError):
            BoxId(id)

    def test_id_random(self):
        for __ in range(10):
            try:
                BoxId.get_random_box_id()
            except (IdWrongLength, IdNotAlphabetic, TypeError) as e:
                self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
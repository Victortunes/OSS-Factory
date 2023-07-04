import unittest
import utils

class TestUtilsOccurencePerChar(unittest.TestCase):

    def test_valid(self):
        expected = {'a':2, 'b':1, 'c':3}
        actual = utils.occurence_per_char('cacbac')
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        occurence_per_letter = utils.occurence_per_char('')
        self.assertEqual({}, occurence_per_letter)

    def test_wrong_datatype(self):
        with self.assertRaises(TypeError):
            utils.occurence_per_char(1) # type: ignore


class TestUtilsIsContainingExactlyXNumberOfAnyChar(unittest.TestCase):

    def test_valid(self):
        test_text = 'cacbac'
        number_of_occurences_with_expected: dict[int,bool] = {1:True, 2:True, 3:True, 4:False, 5:False}

        for number_of_occurences, expected in number_of_occurences_with_expected.items():
            actual = utils.is_containing_exactly_x_number_of_any_char(test_text, number_of_occurences)
            self.assertEqual(actual, expected, msg=f'Error during testing this number of occurences {number_of_occurences}')

    def test_empty_string(self):
        self.assertEqual(utils.is_containing_exactly_x_number_of_any_char('', 1), False)

    def test_wrong_text_datatype(self):
        with self.assertRaises(TypeError):
            utils.is_containing_exactly_x_number_of_any_char(1,1) # type: ignore

    def test_wrong_occurence_number_datatype(self):
        with self.assertRaises(TypeError):
            utils.is_containing_exactly_x_number_of_any_char('','1') # type: ignore

    def test_occurence_number_out_of_range(self):
        with self.assertRaises(ValueError):
            utils.is_containing_exactly_x_number_of_any_char('',0)


class TestUtilsTextSimiliraties(unittest.TestCase):

    def test_valid(self):
        expected = 'fgij'
        similiraties = utils.text_similiraties('fghij','fguij')
        self.assertEqual(expected, similiraties)

    def test_inequal_texts_lengths(self):
        with self.assertRaises(ValueError):
            utils.text_similiraties('a','abc')

    def test_wrong_datatype_text_a(self):
        with self.assertRaises(TypeError):
            utils.text_similiraties(1,'abc') # type: ignore
    
    def test_wrong_datatype_text_b(self):
        with self.assertRaises(TypeError):
            utils.text_similiraties('a',1) # type: ignore

    def test_wrong_datatype_text_a_and_b(self):
        with self.assertRaises(TypeError):
            utils.text_similiraties(1,1) # type: ignore


if __name__ == '__main__':
    unittest.main()
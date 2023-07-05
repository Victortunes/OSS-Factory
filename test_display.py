import unittest
from io import StringIO
import sys
import logging

from display import Display

class TestDisplay(unittest.TestCase):

    def setUp(self) -> None:
        self.__display = Display()
        self.__capturedOutput = StringIO() #redirect and capture print() output
        sys.stdout = self.__capturedOutput    

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__ #reset redirect

    def test_valid_logger_proprerty(self):
        self.assertEqual(type(self.__display.logger), logging.Logger)

    def test_valid_info(self):
        expected = 'abc'
        self.__display.print(expected)
        self.assertIn(expected, self.__capturedOutput.getvalue())

    def test_wrong_datatype_info(self):
        with self.assertRaises(TypeError):
            self.__display.print(1) #type: ignore

    def test_valid_warn(self):
        expected = 'abc'
        with self.assertLogs(level=logging.WARN) as log:
            self.__display.warn(expected)
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn(expected, log.output[0])

    def test_wrong_datatype_warn(self):
        with self.assertRaises(TypeError):
            self.__display.warn(1) #type: ignore

    def test_valid_error(self):
        expected = 'abc'
        with self.assertLogs(level=logging.ERROR) as log:
            self.__display.error(expected)
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn(expected, log.output[0])

    def test_wrong_datatype_error(self):
        with self.assertRaises(TypeError):
            self.__display.error(1) #type: ignore

    def test_valid_title(self):
        self.__display.title('abc', '=', 2)
        self.assertEqual(self.__capturedOutput.getvalue(), '== abc ==\n')

    def test_wrong_message_datatype_title(self):
        with self.assertRaises(TypeError):
            self.__display.title(1) #type: ignore

    def test_wrong_stroke_datatype_title(self):
        with self.assertRaises(TypeError):
            self.__display.title('abc', 1) #type: ignore

    def test_too_long_stroke_title(self):
        with self.assertRaises(ValueError):
            not_a_char = 'a_'
            self.__display.title('abc', not_a_char)

    def test_wrong_stroke_len_datatype_title(self):
        with self.assertRaises(TypeError):
            self.__display.title('abc', stroke_len='1') #type: ignore
    
    def test_out_of_range_stroke_len_title(self):
        with self.assertRaises(ValueError):
            self.__display.title('abc', stroke_len=-1)

    def test_all_invalid_title(self):
        with self.assertRaises( (ValueError, TypeError) ):
            self.__display.title(1,1,'1') #type: ignore

    def test_valid_question_with_answer(self):
        question = '1+1 ?'
        answer = '2'
        arrow = '::>'
        self.__display.question_with_answer(question, answer, arrow)
        actual = self.__capturedOutput.getvalue()

        #content check
        self.assertIn(question, actual)
        self.assertIn(answer, actual)
        self.assertIn(arrow, actual)

        #format check
        splitted_actual = actual.split('\n')
        actual_question = splitted_actual[0]
        actual_answer_with_arrow = splitted_actual[1]

        self.assertEqual(question, actual_question)
        self.assertTrue(actual_answer_with_arrow.startswith(arrow))
        self.assertTrue(actual_answer_with_arrow.endswith(answer))

    def test_wrong_question_datatype_question_with_answer(self):
        with self.assertRaises(TypeError):
            self.__display.question_with_answer(1+1, '2') #type: ignore

    def test_wrong_answer_datatype_answer_with_answer(self):
        with self.assertRaises(TypeError):
            self.__display.question_with_answer('1+1', 2) #type: ignore

    def test_wrong_arrow_datatype_questin_with_answer(self):
        with self.assertRaises(TypeError):
            self.__display.question_with_answer('1+1', '2', 1) #type: ignore

    def test_all_invalid_question_with_answer(self):
        with self.assertRaises(TypeError):
            self.__display.question_with_answer(1+1, 2, 1) #type: ignore

if __name__ == '__main__':
    unittest.main()
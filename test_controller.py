import unittest
import os
from pathlib import Path

from controller import Controller, NotAFile, PathNotExists
from display import Display

class TestInitController(unittest.TestCase):

    def test_valid_init(self):
        Controller(Display())

    def test_wrong_datatype_init(self):
        with self.assertRaises(TypeError):
            Controller('display') #type: ignore        

class TestController(unittest.TestCase):

    def setUp(self):
        self.__controller = Controller(Display())

    def test_valid_run(self):
        self.__controller.run(str(Path(os.path.dirname(os.path.abspath(__file__)), 'storage/input.txt')))

    def test_wrong_datatype_run(self):
        with self.assertRaises(TypeError):
            self.__controller.run(1) #type: ignore


if __name__ == '__main__':
    unittest.main()
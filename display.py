import logging

class Display:
    """
    A class that used to display content to the user.

    Methods
    -------
    title -> None
        display a title with the provided message
    print -> None
        print the provided message
    warn -> None
        display a warn with the provided message
    error -> None
        display an error with the provided message
    question_with_answer -> None
        display a question with his answer
    
    Property
    --------
    logger -> logging.Logger
        return the logger used by the display
    """

    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)

    def __data_validation_string(self, data:str, data_name:str) -> None:
        """Validate string data, raise an error if not valid"""
        if type(data) is not str: raise TypeError(f'{data_name} must be a string')

    def __data_validation_char(self, data:str, data_name:str) -> None:
        """Validate char data, raise an error if not valid"""
        if type(data) is not str: raise TypeError(f'{data_name} must be a string')
        if len(data) != 1:raise ValueError(f'{data_name} must be one length')

    def __data_validation_int(self, data:int, data_name:str, min:int|None = None, max:int|None = None) -> None:
        """Validate int data with optional range, raise an error if not valid"""
        if type(data) is not int: raise TypeError(f'{data_name} must be an int')
        if min is not None: 
            if data < min: raise ValueError(f'{data_name} must be greater than {min}')
        if max is not None: 
            if data > max: raise ValueError(f'{data_name} must be less than {max}')

    def title(self, title:str, stroke:str = '-', stroke_len:int = 6):
        """display a title with the provided message"""
        self.__data_validation_string(title, 'title')
        self.__data_validation_char(stroke, 'stroke')
        self.__data_validation_int(stroke_len, 'stroke_len', min=0)
        title = f' {title} '
        title = stroke*stroke_len + title + stroke*stroke_len
        self.print(title)

    def print(self, message:str):
        """print the provided message"""
        self.__data_validation_string(message, 'message')
        print(message)

    def warning(self, message:str):
        """display a warn with the provided message"""
        self.__data_validation_string(message, 'message')
        logging.warning(f' {message}')

    def error(self, message:str):
        """display an error with the provided message"""
        self.__data_validation_string(message, 'message')
        logging.error(f' {message}')

    def question_with_answer(self, question:str, answer:str, answer_arrow:str='=>'):
        """display a question with his answer"""
        self.__data_validation_string(question, 'question')
        self.__data_validation_string(answer, 'answer')
        self.__data_validation_string(answer_arrow, 'answer_arrow')

        self.print(question)
        self.print(f'{answer_arrow} {answer}')

    @property
    def logger(self) -> logging.Logger:
        """return the logger used by the display"""
        return logging.getLogger(__name__)

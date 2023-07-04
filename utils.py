def occurence_per_char(text: str) -> dict[str,int]:
    """return a dict with letter as key associated with the number of occurences

    Parameters
    ----------
        text : str
            text to parse
    """
    if type(text) is not str: raise TypeError('text must be a string')
    occurence_per_letter: dict[str,int] = {}

    for letter in text:
        occurence = text.count(letter)
        if occurence > 0:
            text.replace(letter, '')
            occurence_per_letter[letter] = occurence
            
    return occurence_per_letter

def is_containing_exactly_x_number_of_any_char(text: str, occurence_number: int) -> bool:
    """return True if the letter is exactly present the number of time specified else False

    Parameters
    ----------
        text : str
            text to parse
        occurence_number : int
            the number of time that the letter should be present
    """
    if type(text) is not str: raise TypeError('text must be a string')
    if type(occurence_number) is not int: raise TypeError('occurence_number must be an integer')
    if occurence_number < 1: raise ValueError('occurence_number must be greater than 0')
    occurence_per_letter = occurence_per_char(text)
    return occurence_number in occurence_per_letter.values()


def common_letters(text_a: str, text_b: str) -> str:
    """return the common letters between two strings

    Parameters
    ----------
        text_a : str
            text to extract common letters with text_b
        text_b : 
            text to extract common letters with text_a
    """
    if type(text_a) is not str or type(text_b) is not str: raise TypeError('text must be a string')
    if len(text_a) != len(text_b): raise ValueError('text_a and text_b must have the same length')
    common_letters = ''

    for i, letter_a in enumerate(text_a):
        letter_b = text_b[i]
        if letter_a == letter_b: common_letters += letter_a
    
    return common_letters


def text_distance(text_a: str, text_b: str) -> int:
    """return the number of different char between two strings

    Parameters
    ----------
        text_a : str
            text to extract to find distance with text_b
        text_b : 
            text to extract to find distance with text_a
    """
    if type(text_a) is not str or type(text_b) is not str: raise TypeError('text must be a string')
    if len(text_a) != len(text_b): raise ValueError('text_a and text_b must have the same length')
    distance = 0

    for i, letter_a in enumerate(text_a):
        letter_b = text_b[i]
        if letter_a != letter_b: distance +=1
    
    return distance
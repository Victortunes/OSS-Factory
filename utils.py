def occurence_per_char(text: str) -> dict[str,int]:
    if type(text) is not str: raise TypeError('text must be a string')
    occurence_per_letter: dict[str,int] = {}

    for letter in text:
        occurence = text.count(letter)
        if occurence > 0:
            text.replace(letter, '')
            occurence_per_letter[letter] = occurence
            
    return occurence_per_letter

def is_containing_exactly_x_number_of_any_char(text: str, occurence_number: int) -> bool:
    if type(text) is not str: raise TypeError('text must be a string')
    if type(occurence_number) is not int: raise TypeError('occurence_number must be an integer')
    if occurence_number < 1: raise ValueError('occurence_number must be greater than 0')
    occurence_per_letter = occurence_per_char(text)
    return occurence_number in occurence_per_letter.values()

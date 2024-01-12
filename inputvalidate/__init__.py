import re

def get_int(prompt, **kwargs):
    """
    Prompts user for an input, expecting an int
    Repeats until an int is properly inputted, then returns the int

    **kwargs:
    min: Set min value acceptable
    max: Set max value acceptable
    """
    while True:
        user_input = input(prompt)

        # if input contains digits
        if re.search(r"\d", user_input):
            # Try converting the string type input into an int
            try:
                user_input = int(user_input)
            # Having '.', or anything other than digits in the string type input will throw an exception
            except ValueError:
                continue
            else:
                if kwargs:
                    if 'min' in kwargs:
                        if user_input >= float(kwargs['min']):
                            pass
                        else:
                            continue
                    
                    if 'max' in kwargs:
                        if user_input <= float(kwargs['max']):
                            pass
                        else:
                            continue
                    
                    return user_input
                
                else:
                    return user_input


def get_float(prompt, **kwargs):
    '''
    Prompts user for an input, expecting a float
    Repeats until an float is properly inputted, then returns the float

    **kwargs:
    min: Set min value acceptable
    max: Set max value acceptable
    '''
    while True:
        user_input = input(prompt)

        # if input contains digits
        if re.search(r"\d", user_input):
            # Try converting the string type input into an int
            try:
                user_input = float(user_input)
            # Having anything other than digits or at most 1 '.' in the string type input will throw an exception
            except ValueError:
                continue
            else:
                if kwargs:
                    if 'min' in kwargs:
                        if user_input >= float(kwargs['min']):
                            pass
                        else:
                            continue
                    
                    if 'max' in kwargs:
                        if user_input <= float(kwargs['max']):
                            pass
                        else:
                            continue
                    
                    return user_input
                
                else:
                    return user_input


def get_number(prompt, **kwargs):
    '''
    Prompts user for an input, expecting a number
    Returns an int or float depending on the number inputted
    Repeats until an number is properly inputted, then returns the number

    **kwargs:
    min: Set min value acceptable
    max: Set max value acceptable
    '''
    while True:
        user_input = input(prompt)

        # Check if input contains digits
        if re.search(r"\d", user_input):
            # Determine if it is an int or float
            try:
                user_input = int(user_input)

            except ValueError:
                # Input may be a float
                try:
                    user_input = float(user_input)
                except ValueError:
                    # Input is neither an int nor float
                    continue

            finally:
                if kwargs:
                    if 'min' in kwargs:
                        if float(user_input) >= float(kwargs['min']):
                            pass
                        else:
                            continue
                    
                    if 'max' in kwargs:
                        if float(user_input) <= float(kwargs['max']):
                            pass
                        else:
                            continue
                    
                    return user_input
                
                else:
                    return user_input


def get_string(prompt, **kwargs):
    """
    Prompts user for an input, expecting a string
    Repeats until an string is properly inputted, then returns the string

    **kwargs:
    min: Set min length acceptable
    max: Set max length acceptable
    nospace: Set to True if input must contain no spaces. Default: False
    """
    while True:
        try:
            user_input = str(input(prompt))
        except ValueError:
            continue
        else:
            if kwargs:
                if 'min' in kwargs:
                    if len(user_input) >= float(kwargs['min']):
                        pass
                    else:
                        continue
                
                if 'max' in kwargs:
                    if len(user_input) <= float(kwargs['max']):
                        pass
                    else:
                        continue
                
                if 'nospace' in kwargs:
                    if kwargs['nospace'] and ' ' in user_input:
                        continue
                
                return user_input
            
            else:
                return user_input


def get_bool(prompt):
    """
    Prompts user for a True/False answer
    Repeats until user inputs True or False, ignoring caps, then returns True or False
    """
    while True:
        user_input = input(prompt)

        if user_input.title() == 'True':
            return True
        elif user_input.title() == 'False':
            return False


def get_yesno(prompt):
    """
    Prompts user for a yes/no answer
    Repeats until the first letter of the input is y/n, ignoring caps, then returns 'y' / 'n'
    """
    while True:
        user_input = input(prompt)

        if user_input[0].lower() == 'y':
            return 'y'
        elif user_input[0].lower() == 'n':
            return 'n'


def get_tf(prompt):
    """
    Prompts user for a True/False answer given as t/f
    Repeats until the first letter of the input is t/f, ignoring caps, then returns True or False
    """
    while True:
        user_input = input(prompt)

        if user_input[0].lower() == 't':
            return True
        elif user_input[0].lower() == 'f':
            return False


def get_word(prompt):
    """
    Prompts user for a single word of only alphabet letters
    Repeats until a word is properly inputted, then returns the word as a string
    """
    while True:
        user_input = input(prompt)

        if user_input.isalpha():
            return user_input


def get_char(prompt):
    """
    Prompts user for a single ASCII character
    Repeats until a character is properly inputted, then returns the char as a string
    """
    while True:
        user_input = input(prompt)

        if user_input.isascii() and len(user_input) == 1:
            return user_input


# Aliases
def get_yn(prompt):
    """
    Prompts user for a yes/no answer
    Repeats until the first letter of the input is y/n, ignoring caps, then returns 'y' / 'n'
    """
    while True:
        user_input = input(prompt)

        if user_input[0].lower() == 'y':
            return 'y'
        elif user_input[0].lower() == 'n':
            return 'n'



# def test(prompt):
#     """
#     Test function
#     """
#     while True:
#         user_input = input(prompt)

#         return int(user_input)
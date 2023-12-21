import re

def get_int(prompt):
    """
    Prompts user for an input, expecting an int
    Repeats until an int is properly inputted, then returns the int
    """
    while True:
        user_input = input(prompt)

        if re.search(r"\d", user_input):
            try:
                return int(user_input)
            except ValueError:
                pass

def get_string(prompt):
    """
    Prompts user for an input, expecting a string
    Repeats until an string is properly inputted, then returns the string
    """
    while True:
        try:
            return str(input(prompt))
        except:
            pass

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

def get_tf(prompt):
    """
    Prompts user for a True/False answer
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


def test(prompt):
    while True:
        user_input = input(prompt)

        return int(user_input)

print(get_word("prompt: "))
# inputvalidate
A Python library which contains various functions to validate user input

inputvalidation.py
- is the main module containing the various input validation functions

Functions:
    get_int(prompt, **kwargs)
        - Prompts user for an input, expecting an int
        - Repeats until proper input received
        kwargs:
            min: minimum value acceptable
            max: maximum value acceptable

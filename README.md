# inputvalidate


<!-- Badges -->
[![PyPI - Downloads](https://img.shields.io/pypi/dm/inputvalidate?label=PyPi%20downloads)](https://pypi.org/project/inputvalidate/)
[![PyPI - Version](https://img.shields.io/pypi/v/inputvalidate)](https://pypi.org/project/inputvalidate/)
<!--tests passing-->
<!--sponser me-->
<!--another badge-->

Do you always find yourself having to write extra code every project to validate the input given by users? Then use inputvalidate -
a Python package containing various functions to validate user input.

Calvin Chan  calvinchan4370z@gmail.com  MIT License

</br>

# Example Usage
Code:
```python
from inputvalidate import get_int

user_age = get_int('Your age (0-99 yrs): ', min=0, max=99)
print(f'You are {user_age} years old.')
```
Terminal:
```
Your age (0-99 yrs): twelve
Your age (0-99 yrs): 20.5
Your age (0-99 yrs): -2
Your age (0-99 yrs): 16
You are 16 years old.
$ |
```

</br>

<!-- # Documentation -->

# Functions
<!-- <button>Open all</button> -->
<!-- get_int -->
## get_int

```python
get_int(prompt, **kwargs)
```
Prompts user for an input, expecting an int. Repeats until an int is properly inputted, then returns the int.

### *kwargs:*
- **min**: Set min value acceptable
- **max**: Set max value acceptable


<!-- get_float -->
## get_float

```python
get_float(prompt, **kwargs)
```
Prompts user for an input, expecting a float. Repeats until a number is properly inputted, then returns the input as a float.

### *kwargs:*
- **min**: Set min value acceptable
- **max**: Set max value acceptable


<!-- get_number -->
## get_number

```python
get_number(prompt, **kwargs)
```
Prompts user for a number. Repeats until a number is properly inputted, then returns the input as an int/float, depending on what was inputted.

### *kwargs:*
- **min**: Set min value acceptable
- **max**: Set max value acceptable


<!-- get_string -->
## get_string

```python
get_string(prompt, **kwargs)
```
Prompts user for an input, expecting a string. Repeats until an string is properly inputted, then returns the string

### *kwargs:*
- **min**: Set min length acceptable
- **max**: Set max length acceptable
- **nospace**: Set to True if input must contain no spaces. Default: False


<!-- get_bool -->
## get_bool

```python
get_bool(prompt)
```
Prompts user for a True/False answer. Repeats until user inputs True or False, ignoring caps, then returns True or False


<!-- get_yesno -->
## get_yesno

```python
get_yesno(prompt)
```
Prompts user for a yes/no answer. Repeats until the first letter of the input is y/n, ignoring caps, then returns 'y' / 'n'

### *Aliases*:
- get_yn


<!-- get_tf -->
## get_tf

```python
get_tf(prompt)
```
Prompts user for a t/f answer. Repeats until the first letter of the input is t/f, ignoring caps, then returns 't' / 'f'


<!-- get_word -->
## get_word

```python
get_word(prompt)
```
Prompts user for a single word of only alphabet letters. Repeats until a word is properly inputted, then returns the word as a string


<!-- get_char -->
## get_char

```python
get_char(prompt)
```
Prompts user for a single ASCII character. Repeats until a character is properly inputted, then returns the char as a string
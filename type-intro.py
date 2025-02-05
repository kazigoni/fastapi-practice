from typing import Optional

# https://fastapi.tiangolo.com/python-types

# type hint


def full_name(fast_name: str, last_name: str):
    '''
    In this funtion we are adding type hing e.g. fast_name: str (colorn and type of data.)
    After typing fast_name when press 'Ctrl+Space' we see options
    that not usually available without declaring 'type hint'. Example available options are
    title(), upper() etc.
    Simple types include - int, float, bool, bytes

    '''
    fullname = fast_name.title() + " " + last_name.upper()
    return fullname


# Simple types ( str, int, float, bool, bytes)
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


# type parameters, data structer (dict, list, set, tuple)
# internal values can have their own type too of these data structures
# No need to declare 'type annotation' by importing 'typing module' in the newer version of Python
# [str] is type parameter for the 'list' data structure in 'items' variable below.
def process_items(items: list[str]):
    '''
    Those internal types in the square brackets are called "type parameters".
    In this case, 'str' is the 'type parameter' passed to List (or list in Python 3.9 and above).

    '''
    # "the variable 'items' is a 'list', and each of the items in this list is a 'str'".
    for item in items:
        print(item)
# If you use Python 3.9 or above, you 'don't have to import List from typing', you can use the same regular list type instead.


'''LIST'''


def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):  # Tuple and Set
    '''This means:

    The variable items_t is a tuple with 3 items, an int, another int, and a str.
    The variable items_s is a set, and each of its items is of type bytes.'''
    return items_t, items_s


'''DICTIONARY'''


def process_items(prices: dict[str, float]):
    ''' Dict-
    To define a dict, you pass 2 type parameters, separated by commas.
    The first type parameter is for the keys of the dict.
    The second type parameter is for the values of the dict:'''
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


'''UNION - Possible type, Below 2 possible value types are acceptable for 'item'. Which are 'int | str' '''


def process_item(item: int | str):  # item could be a 'int' or 'str' value
    print(item)

# from typing import Optional


# Possibly 'None'
# Python 3.6 to Python 3.10
def say_hi(name: Optional[str] = None):
    '''A value could be 'str' or 
        could also ba a 'None' '''
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("No Name, Hello world")


# Python 3.10+, you can use 'Something | None'
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("No Name, Hello world")


# GENERIC TYPE - TAKES PARAMETERS IN SQUARE BRACKETS
'''
These types that take type parameters in square brackets are called Generic types or Generics, for example:

list
dict
set
tuple

In Python 3.10, as an alternative to using the generics Union and 'Optional', 
you can use the 'vertical bar (|)' to declare unions of types, that's a lot better and simpler

'''


# Classes as types
'''Classes as types'''

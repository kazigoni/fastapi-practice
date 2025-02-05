# https://fastapi.tiangolo.com/python-types
# type hint
def full_name(fast_name: str, last_name: str):
    '''
    In this funtion we are adding type hing e.g. fast_name: str (colorn and type of data.)
    After typing fast_name when press Ctrl+Space we see options 
    that not usually available without declaring 'type hint'

    '''
    fullname = fast_name.title() + " " + last_name.upper()
    return fullname

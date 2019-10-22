'''
Dit is een module met functies
'''

def foo():
    '''
    >>> foo()
    'foo'

    >>> fooWaarde = foo()
    >>> fooWaarde
    'foo'

    '''
    return 'foo'

def functie_zonder_return():
    '''
    >>> functie_zonder_return()

    '''

def functie_met_parameter(a):
    '''
    >>> a=3
    >>> functie_met_parameter(a)
    >>> a
    3
    '''
    a += 1

def moet_list_zijn(lijst:list):
    '''
    #>>> moet_list_zijn(1)
    TypeError
    '''
    if not isinstance(lijst, list):
        raise TypeError()
    pass

def functie_met_stackoverflow():
    functie_met_stackoverflow()

def return_in_loop():
    while True:
        return 'iuy'

if __name__ == '__main__':
    print('De module is geladen als script')

    # waarde = functie_zonder_return()

    # moet_list_zijn(44)

    # functie_met_stackoverflow()
    return_in_loop()
    pass

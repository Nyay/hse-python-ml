#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def reverse_dictionary(dictionary):
    """
    Function reverses dictionary with structure { key: [values] } to
    dictionary with structure {value: [keys]}.

    >>> d = reverse_dictionary( {1: [4], 2: [3]} )
    >>> d == {3: [2], 4: [1]}
    True
    >>> d = reverse_dictionary( {1: [3, 4, 5]} )
    >>> d == {3: [1], 4: [1], 5: [1]}
    True
    >>> d == reverse_dictionary( {'hello': ['привет', 'здравствуй'], 'python': ['питон'] })
    >>> d == {'здравствуй': ['hello'], 'привет': ['hello'], 'питон': ['python']}
    True
    """
    raise NotImplementedError


def parse_dictionary(text):
    """
    Function forms dictionary from input text.

    >>> d = parse_dictionary('мама - mommy')
    >>> d == {'мама': ['mommy']}
    True
    >>> d = parse_dictionary('hello - привет, здравствуй')
    >>> d == {'hello': ['привет', 'здравствуй']}
    True
    >>> d = parse_dictionary('hello - привет, здравствуй, здорова')
    >>> d = {'hello': ['привет', 'здравствуй', 'здорова']}
    True
    >>> d = parse_dictionary("мама - mommy, mom\\nпапа - daddy, father")
    >>> d == {'мама': ['mommy', 'mom'], 'папа': ['daddy', 'father']}
    True
    >>> d = parse_dictionary("сын - son\\nпапа - daddy, father")
    >>> d == {'сын': ['son'], 'папа': ['daddy', 'father']}
    True
    """
    raise NotImplementedError


def print_dictionary(dictionary):
    with open('output.txt', 'w') as out:
        for key in sorted(dictionary):
            print(key + ' - ' + ', '.join(dictionary[key]), file=out)


def main():
    text = sys.stdin.read()
    base_dictionary = parse_dictionary(text)
    reversed_dictionary = reverse_dictionary(base_dictionary)
    print_dictionary(reversed_dictionary)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

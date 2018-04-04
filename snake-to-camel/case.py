"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    camel_variable = []
    i = 0

    while i < len(variable_name):
        if variable_name[i] == '_':
            camel_variable.append(variable_name[i + 1].upper())
            i += 2
        else:
            camel_variable.append(variable_name[i])
            i += 1

    return ''.join(camel_variable)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"

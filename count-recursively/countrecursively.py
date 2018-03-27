"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst, start_index=0):
    """Return number of items in a list, using recursion."""

    # naive solution
    # base case
    # if not lst:
    #     return 0

    # return 1 + count_recursively(lst[1:])

    # better runtime

    # base case
    if start_index == len(lst):
        return 0

    return 1 + count_recursively(lst, start_index=start_index+1)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"

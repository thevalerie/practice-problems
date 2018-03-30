"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    position = 0
    leaps = 0

    # while the lemur is not at the third-to-last branch
    while position < len(branches) - 3:
        # check to see if the lemur can leap two branches
        if branches[position + 2]:
            position +=1
        # otherwise, just leap one
        else:
            position += 2
            # branches_left -= 2
        leaps += 1

    # once we get to the third-to-last or second-to-last branch, add one more leap to the end
    if position < (len(branches) - 1):
        leaps += 1

    return leaps
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"
"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    # create a dict for bracket pairs
    pairs = {
             ')':'(',
             '}':'{',
             ']':'[',
             '>':'<'
             }

    # create a set of open brackets
    open_brackets = set(pairs.values())

    # create a stack for unbalanced open brackets
    bracket_stack = []

    # loop through the phrase
    for char in phrase:
      # if we find a closing bracket, check if the last open bracket is its pair
      if char in pairs:
        if bracket_stack and pairs[char] == bracket_stack[-1]:
          bracket_stack.pop()
        # if we don't have a corresponding open bracket, fail fast
        else:
          return False
      # if we find an opening bracket, add it to the stack
      if char in open_brackets:
        bracket_stack.append(char)

    # if the stack is empty, the string is balanced
    return not bracket_stack


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"

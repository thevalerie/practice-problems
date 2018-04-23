"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        def subtree_is_valid(node, left_min, right_max):
            """Helper function to call recursively on sub-trees"""

            # base case when we've hit a leaf and the upstream tree has not been invalidated
            if node is None:
                return True

            # check to make sure that the node's data is within valid sub-tree boundaries
            if not left_min < node.data < right_max:
                # if not, fail fast
                return False

            # call the function recursively on the left child, with the current data as new max
            if not subtree_is_valid(node.left, left_min, node.data):
                # if the recursive function returns False, fail fast
                return False

            # same on the right child, resetting the min
            if not subtree_is_valid(node.right, node.data, right_max):
                return False

            # if we get past the invalidations, return true
            return True

        # call the helper function on the root node with negative and positive infinity to start
        return subtree_is_valid(self, left_min=float('-inf'), right_max=float('inf'))


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"

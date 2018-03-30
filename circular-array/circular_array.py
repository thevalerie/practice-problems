"""Implement a Circular Array

A circular array is defined by having a start and indexes (be
sure to think about optimizing runtime for indexing)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.print_array()
    harry
    hermione
    ginny
    ron
    >>> circ.get_by_index(2)
    'ginny'
    >>> print circ.get_by_index(15)
    None

However, the last item circles back around to the first item, 
so you can also rotate the list and shift the indexes. Positive
numbers rotate the list start to the right (or higher indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(1)
    >>> circ.print_array()
    hermione
    ginny
    ron
    harry
    >>> circ.get_by_index(2)
    'ron'

And negative numbers rotate the list start to the left (or lower
indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-1)
    >>> circ.print_array()
    ron
    harry
    hermione
    ginny
    >>> circ.get_by_index(2)
    'hermione'

And you can also rotate more than once around the ring::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-17)
    >>> circ.get_by_index(1)
    'harry'

If you add a new item after rotating, it should go at the end of
the list in its current rotation::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-2)
    >>> circ.add_item('dobby')
    >>> circ.print_array()
    ginny
    ron
    harry
    hermione
    dobby

"""

#### OPTIMIZED FOR ADDING AN ITEM ####

# class CircularArray(object):
#     """An array that may be rotated, and items retrieved by index"""

#     def __init__(self):
#         """Instantiate CircularArray."""
#         self.data = []

#     def add_item(self, item):
#         """Add item to array, at the end of the current rotation."""

#         self.data.append(item)

#     def get_by_index(self, index):
#         """Return the data at a particular index."""

#         # if index is within the length of the array forward and backward,
#         # return the item at that index
#         if -(len(self.data)) <= index < len(self.data):
#             return self.data[index]

#         # otherwise, return the item at the index of the mod of the index with respect to the length
#         else:
#             return self.data[index % len(self.data)]


#     def rotate(self, increment):
#         """Rotate array, positive for right, negative for left.

#         If increment is greater than list length, keep going around.
#         """
#         rotated_array = []

#         for i in xrange(increment, increment + len(self.data)):
#             item = self.get_by_index(i)
#             rotated_array.append(item)

#         self.data = rotated_array

#     def print_array(self):
#         """Print the circular array items in order, one per line"""

#         for item in self.data:
#             print item


#### OPTIMIZED FOR ROTATING ####

class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""
        self.data = []
        self.head = 0

    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""

        # if the head is 0, append to the data array
        if self.head == 0:
            self.data.append(item)

        else:
            # insert the new item at the current head index
            self.data.insert(self.head, item)
            # reset the head
            self.head += 1


    def get_by_index(self, index):
        """Return the data at a particular index."""

        if index >= len(self.data):
            return None

        location = self.head + index
        
        if location < len(self.data):
            return self.data[location]
        else:
            return self.data[location % len(self.data)]


    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.
        """

        new_head = self.head + increment

        if 0 <= new_head < len(self.data):
            self.head = new_head
        else:
            self.head = new_head % len(self.data)


    def print_array(self):
        """Print the circular array items in order, one per line"""

        for i in xrange(len(self.data)):
            print self.get_by_index(i)

if __name__ == "__main__":
    print
    import doctest

    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED; YOU MUST BE DIZZY WITH JOY! ***"
    print

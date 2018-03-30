"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

### O(n) runtime solution ###

    # nums_left = set(range(1, max_num + 1))

    # for num in nums:
    #     nums_left.remove(num)

    # return nums_left.pop()

### O(1) runspace solution ###

    # nums.sort()

    # for i, num in enumerate(nums):
    #     if num != i + 1:
    #         return i + 1

### O(n) runtime and O(1) runspace ###
    
    expected_sum = max_num * (max_num + 1) / 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"

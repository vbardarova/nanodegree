def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return

    answer = [-float('inf'), float('inf')]
    for _int in ints:
        if _int > answer[0]:
            answer[0] = _int
        if _int < answer[1]:
            answer[1] = _int
    return (answer[1], answer[0])

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((1, 1) == get_min_max( [1] ) ) else "Fail")
print ("Pass" if ((0, 1) == get_min_max([1,0]) ) else "Fail")
print ("Pass" if ((4, 4) == get_min_max([4,4])) else "Fail")
print ("Pass" if ((6, 9) == get_min_max([8,6,9])) else "Fail")

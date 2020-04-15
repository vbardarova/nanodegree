def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)

    return binary_search(input_list, pivot + 1, len(input_list) - 1, number)

def find_pivot(arr, start_index, end_index):
    if start_index > end_index:
        return -1
    if start_index == end_index:
        return start_index

    mid_index = (start_index + end_index) // 2

    if mid_index < end_index and arr[mid_index] > arr[mid_index + 1]:
        return mid_index

    if mid_index > start_index and arr[mid_index] < arr[mid_index - 1]:
        return (mid_index - 1)

    if arr[start_index] >= arr[mid_index]:
        return find_pivot(arr, start_index, mid_index - 1)

    return find_pivot(arr, mid_index + 1, end_index)


def binary_search(array, start_index, end_index, target):
    '''Write a function that implements the binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: initial position to start search
      end_index: last position to end search
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    while start_index <= end_index:
        mid_point = (start_index + end_index) // 2

        mid_item = array[mid_point]

        if target == mid_item:
            return mid_point

        elif target < mid_item:
            end_index = mid_point - 1

        else:
            start_index = mid_item + 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

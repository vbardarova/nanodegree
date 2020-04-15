def sort(input_list, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = input_list[pivot_index]

    while left_index < pivot_index:

        left_value = input_list[left_index]
        
        if left_value < pivot_value:
            left_index += 1
            continue

        input_list[left_index] = input_list[pivot_index-1]
        input_list[pivot_index-1] = pivot_value
        input_list[pivot_index] = left_value
        pivot_index -= 1

    return pivot_index


def sort_all(input_list, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort(input_list, begin_index, end_index)
    sort_all(input_list, begin_index, pivot_index - 1)
    sort_all(input_list, pivot_index + 1, end_index)


def quick_sort(input_list):
    sort_all(input_list, 0, len(input_list)-1)
    return input_list

def rearrange_digits(arr): 
  
    # sort the array 
    sorted_array = quick_sort(arr)
    arr = sorted_array[::-1]
  
    # let two numbers be a and b 
    a = 0; b = 0
    for i in range(len(arr)): 
      
        # Fill a and b with every alternate 
        # digit of input array 
        if (i % 2 != 0): 
            a = a * 10 + arr[i] 
        else: 
            b = b * 10 + arr[i] 
  
    # return the sum 
    return [a,b] 

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])

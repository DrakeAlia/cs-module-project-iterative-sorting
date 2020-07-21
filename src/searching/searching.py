def linear_search(arr, target):
     # loop over every element, one by one
    for i in range(len(arr)): 
        # if the element is equal to the target
        if arr[i] == target: 
            return i
    # target was not in the array, not found
    return -1 

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # declare a starting point
    low = 0 
    # declare an ending point
    high = len(arr)-1 
    # declare a mid point for now
    mid = 0 
    # loop
    while high >= low: 
        # find the mid point
        mid = (high + low) // 2 
        # if the mid point is greater than the target
        if arr[mid] > target:
            # ignore one side of the array 
            high = mid - 1 
            # if the mid point is less than the target
        elif arr[mid] < target: 
            # ignore one side of the array
            low = mid + 1 
            # if the mid point is the target
        else: 
            return mid 
    # target was not in the array, not found
    return -1 
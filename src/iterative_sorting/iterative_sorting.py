# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    # loop through n-1 elements
    # for each element in the array, starting at the first index and finishing at the last index
    for i in range(len(arr) - 1):
        # declare that the smallest index is the current index's value, "grab the first element so we can compare later"
        smallest_index = i 
        # TO-DO: find next smallest element
         # loop through the remainder of the array, starting with the next element and finishing with the last element
        for j in range(i+1, len(arr)):
            # if the element is less than the smallest index element
            if arr[j] < arr[smallest_index]:
                # then make the smallest element that element
                smallest_index = j 
        # TO-DO: swap
        # 1, 0 = 0, 1
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 
    return arr


# TO-DO: Implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through the array
    for i in range(len(arr)):
    # loop through the array, that will leave off the last index, we don't want to loop on the last index
        for j in range(len(arr) - 1):
        # if the first element is bigger than the second element
            if arr[j] > arr[j+1]:
                # swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

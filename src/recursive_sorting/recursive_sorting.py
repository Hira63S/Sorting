# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """ Takes in two arrays and merges them after sorting """
    elements = len(arrA) + len(arrB) # get the elements length of the two arrays
    merged_arr = [0] * elements      # Get a list with 0s that is the same length as total two arrays
    merged_arr =[]                  # make the merged_arr an empty list.

    A_i = 0                # two cursors needed to move around the array
    B_i = 0
    for i in range(0, elements):
        if A_i >= len(arrA):    # if the cursor value is greater than the length, we have reached the end
            merged_arr.append(arrB[B_i])
            B_i = B_i +1

        elif B_i >= len(arrB):  # same for the second cursor
            merged_arr.append(arrA[A_i])
            A_i = A_i + 1

        elif arrA[A_i] <= arrB[B_i]:        # the actual replacement if arrA index is smaller
            merged_arr.append(arrA[A_i])    # we append it to merged_arr
            A_i = A_i + 1                   # move the cursor

        elif arrB[B_i] <= arrA[A_i]:        # same for the other array
            merged_arr.append(arrB[B_i])
            B_i = B_i + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    if len(arr) == 1:                   # if the array lenght if 1, we do not need to divide
        return arr                      # so we just return the array
    if len(arr) > 1:                    # find the middle of array by dividing it by two
        left = merge_sort(arr[0 : len(arr)//2]) # divide to left and right &
        right = merge_sort(arr[len(arr)//2:])   # do merge_sort on left and right, recursion part
        arr = merge(left, right)                # put it back together by doing merge

    return arr



# STRETCH: implement an in-place merge sort algorithm
# need to set cursors
# do comparison
# there would be no merged_arr because we are doing in-place i.e. move the numbers around
# instead of merging to an empy array.
def merge_in_place(arr, start, mid, end):
    # TO-DO


    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

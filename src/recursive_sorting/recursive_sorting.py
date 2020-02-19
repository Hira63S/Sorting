# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """ Takes in two arrays and merges them after sorting """
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    merged_arr =[]

    arrA_index = 0
    arrB_index = 0
    for i in range(0, elements):
        if arrA_index >= len(arrA):
            merged_arr.append(arrB[arrB_index])
            arrB_index = arrB_index +1

        elif arrB_index >= len(arrB):
            merged_arr.append(arrA[arrA_index])
            arrA_index = arrA_index + 1

        elif arrA[arrA_index] <= arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index = arrA_index + 1

        elif arrB[arrB_index] <= arrA[arrA_index]:
            merged_arr.append(arrB[arrB_index])
            arrB_index = arrB_index + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)

    return arr



# STRETCH: implement an in-place merge sort algorithm
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

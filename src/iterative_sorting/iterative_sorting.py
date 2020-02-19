# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index # we make the
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # go all the way to second_last index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]: # everything that is to the right of the index
                smallest_index = j

        # now replace
        new = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = new

    return arr

# Big O notation of n**2
# n(n) -> O(n**2)

# TO-DO:  implement the Bubble Sort function below
# How it works:
# Compare the first two elements in array and compare if the left hand side is bigger
# than the right hand side
# Check if the swap actually happened
# if the left hand side is less than right hand side.
# holding n cards in the hand.
# the largest item is bubbled to the end of the array. We have to repeat the process

def bubble_sort( array ):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j] # if the item at that index is greater than the next one, make it temp
                array[j] = array[j+1] # make the next item in the list a temp[j] item so that when it loops thru, it will compare it with the next one
                array[j+1] = temp # make the new item the temp.
#                array[j], array[j+1] = array[j+1], array[j]
    return array


# array = [30, 43, 9, 89, 40]
# bubble_sort(array)
# print(array)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

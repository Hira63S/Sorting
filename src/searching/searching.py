# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
#    if len(arr) == 0:
#        return -1 # array empty

    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high)//2
        if target < arr[middle]:
            high = middle-1 # move onto the left hand side of the list
        elif target > arr[middle]:
            low = middle+1 # move to the right hand side of the list
        else:
            return middle
    return -1
  # not found

arr = [39, 48, 12, 123, 45, 23, 98, 87, 10, 11]
target = 98
result = binary_search(arr, target)
print(result)

# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

#  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

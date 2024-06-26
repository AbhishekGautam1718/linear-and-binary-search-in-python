def linearSearch(array, target,len_arr):
    ''' what is linear search
        the linear search is basically search the target
        numbers in linear formate just like when we draw a
        strait line then it goes in linear formate'''

    # Going through array sequencially
    for i in range(0, len_arr):
        if (array[i] == target):
            return i
    return -1


array = [2, 4, 0, 1, 9]
target = 1
len_arr=len(array)
print("array of linear search is :",array)
print("Target value is: ",target)
result = linearSearch(array, target,len_arr)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)



def binary_search(arr, low, high, target):
    ''' what is Binary search
        binary search basicaly devided by two subparts of
        array and find middle value and search by larger
        and lower value from the middle value and get target value'''
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2 # formula to find the middle value 
 
        # If element is present at the middle itself
        if arr[mid] == target:
            return mid
 
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, target)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
target = 10
indexing_arr=arr[0]
len_arr=len(arr)-1

print("array for binary search is: ",arr)
print("Target value is: ",target)
# Function call
result = binary_search(arr, indexing_arr, len_arr, target)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


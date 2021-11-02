l=[5,6,7,8,9,10,11,12,13,14]
def binary_search(arr, val):
    left = 0 
    right = len(arr)-1
    mid = (left + right)//2

  #Go through the array
    if (val == arr[mid]):
        return mid
   #Check right side of arr
    if (val > arr[mid]):
        return binary_search(arr[mid+1:], val) + (mid + 1)
   #Check left side of arr
    return binary_search(arr[:mid], val)
print(binary_search(l,8))
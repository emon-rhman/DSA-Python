def binarySearch(arr, target):
    left, right = arr[0], len(arr)-1
    
    while left <= right:
        mid = (left+right)//2
        
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid-1
        else:
            left = mid+1
            
    return -1    
        
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != 1:
    print("Value found at:", result)
else:
    print("Value not found.")
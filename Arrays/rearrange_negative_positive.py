# Time Complexity O(n)
# Auxillary Space O(1)

# A python program to put
# all negative numbers before
# positive numbers in array

def rearrange(arr, n):
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    print("After sorting : ", arr)

# Driver Code
arr = [-1, 2, -3, 4 ,5 , 6, -7 , -8, 9]
n = len(arr)

print("Before sorting : ", arr)
rearrange(arr, n)
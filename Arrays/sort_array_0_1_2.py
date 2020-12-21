# Time Complexity O(n)
# Space Complexity O(1)

# Function to sort 0s, 1s and 2s
def sortArr(arr, n):
    count0 = 0
    count1 = 0
    count2 = 0

    # Count number od 0 1 and 2 in the array
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        elif arr[i] == 2:
            count2 += 1
    
    i = 0

    # Place all 0s in the beginning
    while(count0 > 0):
        arr[i] = 0
        count0 -= 1
        i += 1

    # Place all 1s next
    while(count1 > 0):
        arr[i] = 1
        count1 -= 1
        i += 1
    
    # Place all 2s next
    while(count2 > 0):
        arr[i] = 2
        count2 -= 1
        i += 1

    print("After sort : ", arr)

# Driver code for above function
arr = [1, 2, 0, 0, 1, 0, 2, 1, 2]
n = len(arr)

print("Before sort : ", arr)
sortArr(arr, n)
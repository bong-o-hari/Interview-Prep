# Time complexity O(n)

def getMinMax(arr):
    n = len(arr)

    # If array has even elements then
    # initialize the first two elements as
    # minimum and maximum
    if n % 2 == 0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])

        # set the start index for loop
        i = 2

    # If array has odd number of elements
    # initialize the first element as min and max
    else:
        mx = mn = arr[0]

        # set start index for loop
        i = 1

    # In while loop pick elements in pairs
    # compare the pairs with max and min so far
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])

        # Increment the loop by 2
        # as 2 elements are processed together
        i += 2
    return(mx, mn)


# Driver Code
if __name__ =='__main__':
     
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)
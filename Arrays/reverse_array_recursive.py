# Recursive solution for reversing an array
# Time complexity O(n)


def reverse_arr_rec(Arr, start, end):
    # Checking if start and end come to the same position
    # or start goes ahead of end, then return
    if start >= end:
        return
    # Swapping the values at index start and end
    Arr[start], Arr[end] = Arr[end], Arr[start]
    reverse_arr_rec(Arr, start + 1, end - 1)

# Driver function for the above function
Arr = [1,2,3,4,5,6]
print(Arr)
# Calling the function created above and passing in values
# Initializing start and end indexes as start = 0 and end = n - 1
reverse_arr_rec(Arr, 0, len(Arr)-1)
# Printing the reversed array
print("Reverse : ", Arr)
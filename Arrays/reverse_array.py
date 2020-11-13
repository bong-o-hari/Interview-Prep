# Iterative solution for reversing an array

# Function to reverse Arrar(Arr) from start to end(length of Arr)
def reverse_arr(Arr, start, end):
    while start < end:
        Arr[start], Arr[end] = Arr[end], Arr[start]
        start += 1
        end -= 1

# Driver function for the above function
Arr = [1,2,3,4,5]
print(Arr)
# Calling the function created above and passing in values
# Initializing start and end indexes as start = 0 and end = n - 1
reverse_arr(Arr, 0, len(Arr)-1)
# Printing the reversed array
print("Reversed : ", Arr)
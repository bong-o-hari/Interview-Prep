def reverse_arr_rec(Arr, start, end):
    if start >= end:
        return
    Arr[start], Arr[end] = Arr[end], Arr[start]
    reverse_arr_rec(Arr, start + 1, end - 1)

Arr = [1,2,3,4,5,6]
print(Arr)
reverse_arr_rec(Arr, 0, len(Arr)-1)
print("Reverse : ", Arr)
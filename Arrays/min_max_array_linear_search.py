# Structure used to return two values from getMinMax()
class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr, n):
    minmax = Pair()

    # If there is only one element in the array then that element
    # is the minimum and the maximum value
    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    # If there is more than one element then initialize min and max
    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

# Driver code
if __name__ == "__main__":
    arr = [999, 56, 121, 155, 984, 1]
    minmax = getMinMax(arr, len(arr))
    print("Maximum : ", minmax.max)
    print("Minimum : ", minmax.min)
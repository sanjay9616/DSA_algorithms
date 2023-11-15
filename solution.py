def bubbleSort(Arr):
    n = len(Arr)
    for i in range(n):
        for j in range(n-i-1):
            if (Arr[j] > Arr[j+1]):
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
    return Arr


print(bubbleSort([5, 3, 3, 6, 7, 2]))

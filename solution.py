def insertionSort(Arr):
    n = len(Arr)
    for i in range(1, n):
        temp = Arr[i]
        j = i-1
        while (j >= 0 and Arr[j] > temp):
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j+1] = temp
    return Arr


print(insertionSort([5, 3, 0, 0, 1, 2]))

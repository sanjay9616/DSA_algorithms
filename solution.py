def selectionSort(Arr):
    n = len(Arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if (Arr[j] < Arr[minimum]):
                minimum = j
        if(minimum != i):
            Arr[i], Arr[minimum] = Arr[minimum], Arr[i]
    return Arr


print(selectionSort([5, 3, 0, 0, 1, 2]))

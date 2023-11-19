def shellSort(Arr):
    n = len(Arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = Arr[i]
            j = i
            while j >= gap and Arr[j - gap] > temp:
                Arr[j] = Arr[j - gap]
                j -= gap
            Arr[j] = temp
        gap //= 2
    return Arr


print(shellSort([-1, 3, 0, 0, 1, 2]))

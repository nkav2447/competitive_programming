def insertionSort1(n, arr):
    temp = arr[len(arr)-1]
    curr = n - 1
    while curr > 0 and arr[curr-1] > temp:
        arr[curr] = arr[curr-1]
        print(*arr)
        curr -= 1
    arr[curr] = temp
    print(*arr)

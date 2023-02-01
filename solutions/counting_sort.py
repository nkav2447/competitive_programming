def countingSort(arr):
    res = [0]*100
    for i in arr:
        res[i] += 1
    return res 

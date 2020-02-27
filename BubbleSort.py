def BubbleSort(arr):
    for n in range(len(arr)):
        finish = True
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                finish = False
        if(finish): return arr
    return arr
print(BubbleSort([4,6,1,3,8,5]))

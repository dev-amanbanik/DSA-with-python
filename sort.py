def quick_sort(arr, low, high):

    if low < high:
        p = partition_low(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

############ when last element is pivot ###############
def partition_High(arr, low, high):                 
    pivot = arr[high]       
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

############# when first element is pivot.##############
def partition_low(arr, low, high):                  
    pivot = arr[low]

    i = low + 1
    j = high

    while i <= j:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


arr = [6, 3, 8, 5, 2, 7,1,4,2,3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [50, 20, 70, 10, 40, 60, 30]

print(quick_sort(arr))
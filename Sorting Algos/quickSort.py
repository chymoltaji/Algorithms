def split(array):
    pivot = 0
    n = len(array)
    low, high = [], []
    for i in range(n):
        if array[i] < array[pivot]:
            low.append(array[i])
        else:
            high.append(array[i])
    return low, high

def quickSort(array):
    low, high = split(array)
    print(low, high)
    if (len(low) != 0 and len(high) > 0):
        quickSort(high)
    elif (len(low) > 0 and len(high) != 0):
        quickSort(low)
    elif (len(low) > 0 and len(high) > 0):
        quickSort(low)
        quickSort(high)
    return array

arr = [13, 15, 2017, 17, 3, 7, 1, 2, 9, 22]
correct = [1, 2, 3, 7, 9, 13, 15, 17, 22, 2017]

result = quickSort(arr)
if result == correct:
    print(f"CORRECT: Sorted to {result}")
else:
    print(f"INCORRECT: Sorted to {result}")
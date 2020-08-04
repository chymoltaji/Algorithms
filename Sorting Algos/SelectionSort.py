def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

arr = [13, 15, 2017, 17, 3, 7, 1, 2, 9, 22]
correct = [1, 2, 3, 7, 9, 13, 15, 17, 22, 2017]

result = selection_sort(arr)
if result == correct:
    print(f"CORRECT: Sorted to {result}")
else:
    print(f"INCORRECT: Sorted to {result}")
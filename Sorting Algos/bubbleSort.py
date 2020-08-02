def bubbleSort(array):
    n = len(array)
    edit = False
    for i in range(1,n):
        if array[i]<array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            edit = True
    if edit == True:
        bubbleSort(array)
    return array
arr = [0, 2, 15, 2017, 1, 1, 17, 3, 7, 1, 2, 3, 9, 22]
correct = [0, 1, 1, 1, 2, 2, 3, 3, 7, 9, 15, 17, 22, 2017]

result = bubbleSort(arr)
if result == correct:
    print(f"CORRECT: Sorted to\t{result}")
else:
    print(f"INCORRECT: Sorted to\t{result}")
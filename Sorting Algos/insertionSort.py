def sort(array):
    n = len(array)
    for i in range(1,n):
        for j in range(n):
            if array[i] <= array[j]:
                value = array.pop(i)
                array.insert(j, value)
    result = array
    return result

arr = [0, 2, 15, 2017, 1, 1, 17, 3, 7, 1, 2, 3, 9, 22]
correct = [0, 1, 1, 1, 2, 2, 3, 3, 7, 9, 15, 17, 22, 2017]
result = sort(arr)
if result == correct:
    print(f"CORRECT: Sorted to\t{result}")
else:
    print(f"INCORRECT:Sorted to\t{result}")
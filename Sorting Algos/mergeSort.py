def sort(array):
    return array

arr = [0, 2, 15, 2017, 1, 1, 17, 3, 7, 1, 2, 3, 9, 22]
correct = [0, 1, 1, 1, 2, 2, 3, 3, 7, 9, 15, 17, 22, 2017]

result = sort(arr)
if result == correct:
    print(f"CORRECT:\t{arr}\nSorted to:\t{result}")
else:
    print(f"INCORRECT:\t{arr}\nsorted to:\t{result}")
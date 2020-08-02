def mergeSort(array):
    n = len(array)
    if n > 1:
        mid = n//2
        left = array[:mid]
        right = array[mid:]
        array = []
        left = mergeSort(left)
        right = mergeSort(right)
        # print (mid, left, right)
        
        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                array.append(left[0])
                left.pop(0)
            else:
                array.append(right[0])
                right.pop(0)

        for i in left: 
            array.append(i) 
        for i in right: 
            array.append(i) 
    
    return array

arr = [0, 2, 15, 2017, 1, 1, 17, 3, 7, 1, 2, 3, 9, 22]
correct = [0, 1, 1, 1, 2, 2, 3, 3, 7, 9, 15, 17, 22, 2017]

result = mergeSort(arr)
if result == correct:
    print(f"CORRECT: Sorted to {result}")
else:
    print(f"INCORRECT: Sorted to {result}")
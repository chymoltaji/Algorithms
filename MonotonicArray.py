# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]
D = [2, 5, 1, 7, 9, 1, 4]

test_list = [A, B, C, D]

def isMonotonic(array):
    increasing = 0
    decreasing = 0
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            increasing += 1
        elif array[i] > array[i+1]:
            decreasing += 1

    if increasing == 0:
        print("True \t |increasing")
    elif decreasing == 0:
        print("True \t |decreasing")
    else:
        print("False \t |not monotonic")

    # print(increasing, decreasing)
        
for test in test_list:
    isMonotonic(test)
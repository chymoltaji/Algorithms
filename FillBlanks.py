#  Given an array containing None values fill in the None values with most recent 
# non None value in the array 
array1 = [1, None, 2, 3, None, None, 5, None]

def fill_blanks(array):
    for i in range(len(array)):
        if array[i] == None:
            array[i] = array1 [i-1]
    print(array)
fill_blanks(array1)
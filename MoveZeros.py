#Given an array nums, write a function to move all zeroes to the end of it 
# while maintaining the relative order of the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(0)
            array.append(0)
    print(array)

move_zeros(array1)
move_zeros(array2)
def binary_search(array, lookup, low, high):
    mid = (high+low)//2
    if high >= low:
        if  array[mid] == lookup:
            return mid
        elif array[mid] > lookup:
            return binary_search(array, lookup, 0, mid-1)
        else:
            return binary_search(array, lookup, mid+1, high)
    else:
        return ("NOT FOUND")

ordered_list = [0, 1, 3, 7, 8, 9, 10, 17, 20, 22, 24, 42, 56, 89, 90]
value = 4
mid = binary_search(ordered_list, value, 0, len(ordered_list)-1)
if mid == "NOT FOUND":
    print("Value not in list")
else:
    print(f"Value {value} found at index: {mid}")
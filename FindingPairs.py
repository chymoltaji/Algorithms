def findging_pairs(array, target):
    n = len(array)
    dictionary = {}
    for i in range(n):
        dictionary[array[i]] = 1
    for  j in range(n):
        test = target - array[j]
        try:     
            if dictionary[test] == 1:
                return f"Found target {target} from sum of {array[j]} and {test}"
        except:
            pass
    return f"Target {target} not found"
arr = [1, 2, 17, 8, 9, 13, 3, 5, 111]
t1 = 116
t2 = 8
t3 = 200

print (findging_pairs(arr, t1))
print (findging_pairs(arr, t2))
print (findging_pairs(arr, t3))

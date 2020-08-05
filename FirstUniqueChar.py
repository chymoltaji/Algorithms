# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def first_unique_char(string):
    i=0
    for char in string:
        count = 0
        i+=1
        for j in string:
            if char == j:
                count += 1
        if count == 1:
            return (print(f"True at {i}, character {char}"))
    return ("-1", "Not found")

first_unique_char("abcdcba") #print d
first_unique_char("qhqqwhokaowiqwralkmgn") #print i
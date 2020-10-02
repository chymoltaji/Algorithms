# Write a method which finds the maximum of two numbers. You should not use if-
# else or any other comparison operator.
import math

def max_no_if(n1, n2):
    try:
        math.sqrt(n1-n2)
    except:
        return n2
    return n1

print(max_no_if(5,12))
# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

n = 35

def prime_array(num_in):
    result = []
    for i in range(1, num_in):
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            result.append(i)
    print(result)
prime_array(n)

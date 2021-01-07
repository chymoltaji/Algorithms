"""
CHALLENGE
Create a hashing algorithm from scratch without outside help
SELF DEFINED REQUIREMENTS
1. Ends in 20 characters regardless of input
2. Independent of the first characters
3. Works both ways
"""
from string import ascii_lowercase as letters

def hash_function(problem):
    options = list((letters[:6] + "".join(map(str, range(10)))))  
    problem = "".join((format(ord(i), 'b') for i in problem))
    
    result = ""
    return result

print(hash_function("aaa"))
print(hash_function("1"))
print(hash_function("6b1"))
print(hash_function("90ttui"))
print(hash_function("helloworld123"))

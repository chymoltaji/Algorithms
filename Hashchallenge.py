"""
CHALLENGE
Create a hashing algorithm from scratch without outside help
SELF DEFINED REQUIREMENTS
1. Ends in 16 characters regardless of input
2. Independent of the first characters
3. Is recursive
"""
from string import ascii_lowercase as letters

N_BUK = 16
OPTIONS = list((letters[:6] + "".join(map(str, range(10)))))
L_OPT = len(OPTIONS)

def hash_function(problem, recur=0):
    '''Hashes given values'''
    bucket, result = [0]*N_BUK, ""
    problem = "".join((format(ord(i), 'b') for i in problem))
    for e, i in enumerate(problem):
        if i == "1":
            bucket[e % N_BUK] += 1
    for j in range(N_BUK):
        result += OPTIONS[((bucket[j]+j+bucket[bucket[j]]*3))%L_OPT]
    if recur == 2:
        return result
    recur += 1
    return hash_function(result, recur)

test_cases = ["1", "6b1", "ds*hbvjjs98", "hello world! 123", "k1@-#djb 21ht js!nka"]
for i in test_cases:
    print(f"\033[0mkey: \033[92m{i:>20} \033[0m --> value: \033[94m{hash_function(i)}")

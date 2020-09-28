# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

    
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#TODO FEEDBACK
# Communication
# [11:06] ok, that’s pretty straight forward.
# [11:08] explain the idea while coding
# [11:10] jump into coding too fast without clear idea on how to solve the problem

# Problem Solving
# [11:09] use list as memory
# [11:19] no time and space complexity analysis

# Coding
# [11:08] start coding
# [11:13] finish coding but the logic is wrong
# [11:16] keep fixing the logic error
# [11:21] Abe to code out the brute force solution

# Verification
# [11:14] give hint -> take it and empty the memory
# [11:16] wrong scope to clear the memory

#TODO Inefficient code
# def longest_substring(s):
#     n = len(s)
#     cache = []
#     memory = []
#     for k in range(n):
#         for i in range(k, n):
#             if s[i] not in memory:
#                 memory.append(s[i])
#             else:
#                 cache.append("".join(memory))
#                 memory = []
#     cache = list(map(len, cache))
#     return max(cache)

# "pwwkew"
#  i
#  j
    
#  longest = 3
#  set([k, e, w])

def longest_substring(s):
    n = len(s)
    memory = set()
    longest = 0
    j = 0
    for i in range(n):
        if j == n:
            break
        if s[i] in memory:
            while s[i] != s[j]:
                j+=1
                memory.remove(s[j])
                longest -= 1
        else:
            memory.add(s[i])
            longest += 1
    return longest
    
s1 = "abcdbhijk" #prints 7
s2 = "bbbbb" #prints 1
s3 = "pwwkew" #print 3
print(longest_substring(s1))
print(longest_substring(s2))
print(longest_substring(s3))


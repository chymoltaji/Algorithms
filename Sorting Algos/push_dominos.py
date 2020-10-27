"""
Solution by Cheyenne Moltaji

Steps:
1. Identify the dominos that are pushed (unnecessary, in step 2)
2. Divide in sub-strings where we omit unaffected dominos
  a. cut before R
  b. cut after L
3. Logic of pushing dominos
  a. R no L     --> all R
  b. L no R     --> all L
  c. L & R & %2 --> half R, half L
  d. L & R else --> half R, mid dot, half L
    
  . L . . R . L R . . . R L . . L . . R . L . R . R . L                              
"""
def partition_s(s):
  """
  Step 2: Partitions s by cutting off before R and after L
  """
  substring = []
  cutoff = 0
  for i in range(len(s)):
    if s[i] == "R":
      substring.append(s[cutoff:i])
      cutoff = i
    elif s[i] == "L":
      substring.append(s[cutoff:i+1])
      cutoff = i+1
    elif s[i] == "." and i == len(s)-1:
      substring.append(s[cutoff:])
  # [print(x) for x in substring]
  return substring

def domino_push(s):
  """
  Step 3: Rewrites partitions of the domino string according to logic:
  R no L     --> all R
  L no R     --> all L
  L & R & %2 --> half R, half L
  L & R else --> half R, mid dot, half L
                  
  Time complexity:  O(n)
  Space complexity: O(n) --> worst case LRLRLRLLLLLRLLLRLL
  """
  sub = partition_s(s)
  for i, item in enumerate(sub):
    n = len(item)
    if ("L" in item) and ("R" not in item):
      sub[i] = "L"*n
    elif ("R" in item) and ("L" not in item):
      sub[i] = "R"*n
    elif ("L" in item) and ("R" in item) and n>3:
      if n%2 == 0:
        sub[i] = ("R"*(n/2) + "L"*(n/2))
      else:
        sub[i] = ("R"*(n//2) + "." + "L"*(n//2))
  result = "".join(sub)
  return result 
     
print(domino_push(".L..R.LR...RL..L..R.L.R.R.L...."))
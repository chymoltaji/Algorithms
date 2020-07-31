# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
  
def reverseInt(n):
    listed = str(n)
    if listed[0]=='-':
        print('-'+ listed[:0:-1])
    else:
        print(listed[::-1])
    
reverseInt(-135) #must print -531
reverseInt(531) #must print 135
reverseInt(13250834) #must print 43805231
reverseInt(-122235) #must print -532221
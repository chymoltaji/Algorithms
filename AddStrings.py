
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

def AddStrings(num1,num2):
    print(int(num1)+int(num2))

AddStrings('123', '321') #print 444
AddStrings('523', '331') #print 854
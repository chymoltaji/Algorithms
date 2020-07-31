# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def ValidPalindrome(string):
    length = len(string)
    if length%2 == 0:
        midpoint = int((length)/2-1)
        pre_mid = str(string[:midpoint+1])
        post_mid = str(string [midpoint+1:])
    else:
        midpoint = int((length-1)/2)
        pre_mid = str(string[:midpoint])
        post_mid = str(string [midpoint+1:])
    if pre_mid == post_mid[::-1]:
        print("True")
    else:
        print("False")

ValidPalindrome("anna")
ValidPalindrome("stanley yelnats")
ValidPalindrome("Helloworld")
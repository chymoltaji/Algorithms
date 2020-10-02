def anagrams(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    print(list(l1^l2))
    if len(list(l1^l2)) == 0 and len(l1)==len(l2):
        return True

print(anagrams([1,2,3], [1,2,3]))
print(anagrams([1,3], [1,2,3]))
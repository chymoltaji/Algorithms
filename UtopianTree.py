def utopianTree(n):
    height = 1
    for i in range(n):
        if i%2 > 0:
            height += 1
        else:
            height += height
    return height
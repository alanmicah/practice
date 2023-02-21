n = [2, 3, 4, 1, 5]
def miniswaps(n):
    swaps = 0
    # get a dictionary of the current index and values of the current list
    
    # use enumerate to get the index and values or list
    a = dict(enumerate(n,1))

    # then get a inverted version where each key is the value and the value is the index
    b = {v:k for k,v in a.items()}
    # compare the original dictionary with b and swap the values if the key is not equal to the value
    for i in a:
        x = a[i]
        if x != i:
            y = b[i]
            a[y] = x
            b[x] = y
            swaps += 1
    return swaps

print(miniswaps(n))
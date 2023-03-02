arr = [7, 1, 3, 2, 4, 5, 6]
swaps = 0
# store the original values at the index
a = dict(enumerate(arr,1))
print(a)
# go through each item in dict, invert the key and values and store those in new dict
b = {v:k for k,v in a.items()}
print(b)
print('----')
# then go through each item in the original dict,
# if the keys of the dict don't match the count,
# then check the inverted dict


for i in a:
    x = a[i]
    if x != i:
        y = b[i]
        a[y] = x
        b[x] = y
        swaps += 1

print(swaps)

print(a)
print(b)
arr = [7, 1, 3, 2, 4, 5, 6]
swap = 0
# store the original values at the index
a = dict(enumerate(arr,1))

# go through each item in dict, invert the key and values and store those in new dict
b = {v:k for k,v in a.items()}

print(a)
print(b)
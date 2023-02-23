# lists
a = [1,2,3,4,5,6,7]
b = [7,6,5,4,3,2,8]
lista = [10, 11, 12, 13]
# creates new set object
setted = set(a)
print(setted)

# tuples
c = ('a','b','c','d','e','f')
d = ('f','b','c','d','e','g')
e = ('word', 'the', 'truth')

# The zip object yields n-length tuples, 
# where n is the number of iterables passed as positional arguments to zip(). 
# The i-th element in every tuple comes from the i-th iterable argument to zip(). 
# This continues until the shortest argument is exhausted.
zipped = zip(c,d,e)
# zipped = zip(c,d)

print(list(zipped))
# "&" is a bit AND operator (multiplication of the bits)
# so the a in bits AND b in bits
if set(lista) & set(b):
    print(True)
else:
    print(False)
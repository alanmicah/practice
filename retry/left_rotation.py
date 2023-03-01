from hashlib import new
from re import A


amount = 3
arr = [1,2,3,4,5]


def leftrotate(amount, arr):
    a = list(arr)
    newarr = a[amount-1:] + a[:amount-1]
    return newarr

print(leftrotate(amount, arr))
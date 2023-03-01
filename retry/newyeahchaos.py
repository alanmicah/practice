arr = [1,2,4,5,6,7,8,3]

print([p-1 for p in arr])
print('-----')
# print(enumerate((arr)))

Q = [p-1 for p in arr]
moves = 0

# to keep track of the current position and initial position
for i,p in enumerate(arr):
    print(i)
    print(p)
    print('----')
    if i-p > 3:
        print("Too chaotic") 

    # using max(p-2,0) to ensure we don't go below zero
    # not sure why p's value increases (which is why p-2 is needed)
    for j in range(max(p-2,0),i):
        if arr[j] > p:
            moves += 1
print(moves)


def ny_chaos(arr):
    return True

# print(ny_chaos(arr))
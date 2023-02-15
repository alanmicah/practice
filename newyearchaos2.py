# n = [4,1,2,3,5]
# n = [1,2,3,5,4]
n = [2,1,5,3,4]

def nychaos(n):
    moves = 0
    Q = [P-1 for P in n]

    # print(Q)
    # keep tracking i is the index number and P is the value
    for i, p in enumerate(Q):
        # As the value and index should match, this checks if there is difference greater than 2
        # This checks if a value has bribed more than 2 people
        # if p - i > 2:
        #     print('Too chaotic')
        #     return
        # print(range(max(p-1,0),i))
        # print("--")
        # print(range(p))
        # Checks whether the value is greater than the value at the index position
        for j in range(p):
            if Q[j] > p:
                moves += 1

    print(moves)

nychaos(n)
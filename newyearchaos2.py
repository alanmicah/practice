# n = [4,1,2,3,5]
# n = [1,2,3,5,4]
n = [2,1,5,3,4]

def nychaos(q):
    moves = 0 
    Q = [p-1 for p in q]
    for i, p in enumerate(Q):
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if Q[j] > p:
                moves += 1
    print(moves)
nychaos(n)
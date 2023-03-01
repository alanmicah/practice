
l = [1,0,2,3,1,2],[3,2,1,3,2,1],[3,2,1,3,2,1],[3,2,1,3,2,1],[3,2,1,3,2,1],[3,2,1,3,2,1]

def sixbysix(l):
    sum = []
    for i in range(len(l)-2):
        for j in range(len(l)-2):
            sum.append(l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j+1]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2])     
    return max(sum)

print(sixbysix(l))
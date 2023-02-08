from cv2 import Mat


w, h = 6, 6
g, l = 3, 3
HourGlass = [[0 for x in range(w)] for y in range(h)]

Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = 1
Matrix[0][1] = 1
Matrix[0][2] = 1
Matrix[1][1] = 1
Matrix[2][0] = 1
Matrix[2][1] = 1
Matrix[2][2] = 1
Matrix[3][2] = 2
Matrix[3][3] = 4
Matrix[3][4] = 4
Matrix[4][3] = 2
Matrix[5][2] = 1
Matrix[5][3] = 2
Matrix[5][4] = 4

HourGlass[0][0] = 1
HourGlass[0][1] = 1
HourGlass[0][2] = 1
HourGlass[1][1] = 1
HourGlass[2][0] = 1
HourGlass[2][1] = 1
HourGlass[2][2] = 1

arr1 = [0,1,2],[1],[0,1,2]

count = 0
count1 = 3
each = 0
totalPer = 0

for i in Matrix:
    for j in i:
        print(j, end = " ")
    print()

arr2 = []

# for i in range(len(Matrix)-2):
#     print(range(len(Matrix)-2))


for i in range(len(Matrix)-2):
    for j in range(len(Matrix)-2):        
        arr2.append(Matrix[i][j]+Matrix[i][j+1]+Matrix[i][j+2]+Matrix[i+1][j+1]+Matrix[i+2][j]+Matrix[i+2][j+1]+Matrix[i+2][j+2])


# for i in Matrix:
#     for j in i:
#         while count <= len(i)-2 and count <= len(Matrix)-2:
#             for a in HourGlass:
#                 for b in a:
#                     while count1 < len(a)-2:
#                         if b:
#                             each += j
#                         count1 += 1
#                 totalPer = each
#                 count += 1
#                 arr2.append(totalPer)

print(max(arr2))

# sum = []


# for i in range(len(Matrix)-2):
#     for j in range(len(Matrix)-2):
#         sum.append(Matrix[i][j]+Matrix[i][j+1]+Matrix[i][j+2]+Matrix[i+1][j+1]+Matrix[i+2][j]+Matrix[i+2][j+1]+Matrix[i+2][j+2])
        
# print(max(sum))
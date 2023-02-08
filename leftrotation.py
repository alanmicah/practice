d = 4
n = [1,2,3,4,5]
# Create a deep copy. Any changes made to copy doesn't reflect the original
copyn = n.copy()
count = 2
length = len(n)

print(n[0])

while count < d:
    for i in n:
        if count+d >= len(n):
            if (count-len(n))-d < 0:
                print(copyn[-((count-len(n)))-d])
                copyn[-((count+d)-len(n))] = i
            elif (count+d-len(n))+d < len(n): 
                copyn[(count+d-len(n))+d] = i
        else:
            copyn[count+d] = i
        count += 1

print(copyn)
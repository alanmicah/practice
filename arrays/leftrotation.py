d = 4
n = [1,2,3,4,5]
# Create a deep copy. Any changes made to copy doesn't reflect the original
copyn = n.copy()
count = 0
length = len(n)

print(n[0])

# while count < d:
#     for i in n:
#         if count+d >= len(n):
#             if ((count+d) - len(n)-1) == 0:
#                 copyn[count+d] = i
#             else: 
#                 copyn[(count+d) - len(n)-1] = i
#         else:
#             copyn[count+d] = i
#         #     if (count-len(n))-d < 0:
#         #         print(copyn[-((count-len(n)))-d])
#         #         copyn[-((count+d)-len(n))] = i
#         #     elif (count+d-len(n))+d < len(n): 
#         #         copyn[(count+d-len(n))+d] = i
#         # else:
#         #     copyn[count+d] = i
#         count += 1

alist = list(n)

# Find the list from the index before and after the value for amount of rotation.
# Add the list from index to beginning onto the end of the list from index to end.

b = alist[d:]+alist[:d]

print(alist[:d])
print("-----")
print(alist[d:])

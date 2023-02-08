import math
import os
import random
import re
import sys
from turtle import position

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds2(c):
    # Write your code here
    if len(c) == 1: 
        print(len(c))
        return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds2(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds2(c[2:])

def jumpingOnClouds1(c):
    jumps = 0
    count= 0
    if len(c) == 1:
        return 0
    elif len(c) == 2: return 0 if c[1]==1 else 1
    while count < len(c):
        if count+2 < len(c) and c[count+2] == 0:
            count+=2
            jumps+=1
        elif count+1 < len(c) and c[count+1] == 0:
            count+=1
            jumps+=1
        else:
            count += 1
    return jumps


def jumpingOnClouds(c):
    # Write your code here
    position = 1
    count = 0
    for i in c:
        # while position < len(c)-1:
        if i == 0 and c[position] == 0:
            # print(position)
            if c[position-2] == 0:
                continue
            elif c[position-2] != 0 or c[position-2]:
                count += 1
            # if c[position] == 0 and c[position-2] == 0:
            #     count += 1
            # elif c[position] == 0 and c[position-2] != 0:
            #     count += 1
        elif i == 0 and c[position] == 1:
            continue
        elif i == 1 and c[position] == 0:
            count += 1
        position += 1
    return count

c = [0,0,1,0,0,1,0]
a = [0,0,0,1,0,0]
print(jumpingOnClouds1(a))

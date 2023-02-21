def countingValleys(steps, path):
    # Write your code here
    valley = False
    level = 0
    count = 0
    for i in path:
        if i == "D":
            level -= 2
            if level < 0 and valley == False:
                count += 1
                valley = True
        else:
            level += 2
            if level >= 0:
                valley = False
    return count

print(countingValleys(12,'DDUUDDUDUUUD'))
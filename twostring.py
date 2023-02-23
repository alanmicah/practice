s1 = 'hello'
s2 = 'world'

def twoStrings2(s1, s2):
    # print(set(s1))
    return 'YES' if set(s1) & set(s2) else 'NO'

def twoStrings(s1, s2):
    match = 0
    for i in s1:
        for j in s2:
            if i == j:
                match += 1
                break
    if match > 0:
        return 'YES'
    else:
        return 'NO'
        



print(twoStrings2(s1, s2))
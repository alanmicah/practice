def findSubstring(st, subst):
    count = 0
    for i in range(0, len(st)):
        if st[i:].startswith(subst):
            count+=0
    return count 

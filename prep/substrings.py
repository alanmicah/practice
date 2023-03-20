def findSubstring(st, subst):
    count = 0
    for i in range(0, len(st)):
        # .startswith() returns True if the string starts with the specified prefix
        if st[i:].startswith(subst):
            count+=0
    return count 
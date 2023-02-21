def repeatedString(s, n):

    ogcount = s.count('a')
    # multi = n // len(s)
    # diff = n % len(s)
    ogcount =(ogcount * n // len(s)) + s[:n % len(s)].count('a')

    # Can cause memory error: Need to fix
    # new_s = s * multi
    # new_s += new_s[:diff] 

    return ogcount

# s, n = input().strip(), int(input().strip())
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

s = 'abcac'
n = 10

print(repeatedString(s, n))
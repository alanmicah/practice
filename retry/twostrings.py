# s1 = 'and'
# s2 = 'art'

s1 = 'world'
s2 = 'hi'

# if set(s1) & set(s2):
#     print('YES')
# else:
#     print('NO')


def two_strings(s1,s2):
    # sets uses a hashtable
    # hashtables typically have O(1) time complexity
    # if there is/values that match then returns 'YES'
    return 'YES' if set(s1) & set(s2) else 'NO'


print(two_strings(s1 ,s2))
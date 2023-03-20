# In the most basic way, this is what format() does
"""
>>> x = "replaced"
>>> "This is {}!".format(x)
'This is replaced!
"""

def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

    # width = len("{0:b}".format(number))
    # count = 1
    # while count <= number:
    # for i in range(1, number+1):
    #     print((i, oct(i)[2:], hex(i)[2:], "{0:b}".format(i)).format(i, width=width))
        # count+=1
    # return

if __name__ == '__main__':
    n = int(input())
    # print_formatted(n)
    listn = [n]
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(listn)))
    print('Value is:{}'.format(n))

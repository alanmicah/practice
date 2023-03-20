
def solve(s):
    listl = []
    # x = ""
    # for word in s.split():
    #     # listl.append(word.capitalize())
    #     # for i in range(0,len(listl)):
    #     #     listl[i][:1:].capitalize()
    #     x +=  "{} ".format(word.capitalize())
    # return x
    x = ' '.join((word.capitalize() for word in s.split(' ')))
    return x
    # for x in s[:].split():
    #     s = s.replace(x, x.capitalize())
    # return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
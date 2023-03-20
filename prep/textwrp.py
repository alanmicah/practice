import textwrap


import textwrap

# string = "This is a very very very very very very long string."

# print(textwrap.wrap(string))
# print(textwrap.fill(string, 8))

def wrap(string, max_width):
    breaks = textwrap.fill(string, max_width)
    return breaks


if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)

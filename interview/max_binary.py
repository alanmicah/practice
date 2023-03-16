# Maximum optimum a binary

# Still not sure what is maximum optimum of a binary number 
def solve(s):
   length = len(s)
   zeros = s.count('0')
   if zeros < 2:
      return s
   s = s.lstrip('1')
   leading_ones = length - len(s)
   leading_ones += zeros - 1
   trailing_ones = length - leading_ones - 1
   answer_left = '1' * leading_ones
   answer_right = '1' * trailing_ones
   return ''.join([answer_left, '0', answer_right])

# s = "001100"
s = "000111000"
print(solve(s))
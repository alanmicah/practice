# magazine = 'attack at dawn'
# note = 'Attack at dawn'
# magazine = 'give me one grand today night'
# note = 'give one grand today'
# magazine = 'two times three is not four'
# note = 'two times two is four'
magazine = 'ive got a lovely bunch of coconuts'
note = 'ive got some coconuts'

from collections import Counter
# A counter tool is provided to support convenient and rapid tallies
# A Counter is a dict subclass for counting hashable objects. 
# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
print(Counter(magazine) + Counter(note))


magazine  = 'give me one grand today night, night and the night night'
note  = 'give one grand today'

from collections import Counter

# A Counter is a dict subclass for counting hashable objects
# https://docs.python.org/3/library/collections.html#collections.Counter
def ransom_note(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}

def checkMagazine(magazine, note): 
    magazine = magazine.split()
    note = note.split()
    match = 0
    # for each word in the magazine compare it to the words in the note.
    # but we only care about the words that note can match with the magazine,
    # we don't care about the words in the magazine that don't come up in the note
    for i in note:
        for j in magazine:
            if i == j:
                match += 1
                magazine.remove(j)
    if len(note) == match:
        print(len(note))
        print(match)
        print(True)
    else:
        print(len(note))
        print(match)
        print(False)

# checkMagazine(magazine,note)

print(ransom_note(magazine, note))
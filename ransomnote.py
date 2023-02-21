
magazine  = 'give me one grand today night'
note  = 'give one grand today'

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
        return True
    else:
        print(len(note))
        print(match)
        return False

print(checkMagazine(magazine,note))
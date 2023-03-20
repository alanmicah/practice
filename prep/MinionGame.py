# give score for all the substrings each player make using the letters of the given string

def minion_game(s):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(s)):
        # checks if the character is a vowel
        if s[i] in vowels:
            # the length of the substring starting with the vowel
            # is add onto the score
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
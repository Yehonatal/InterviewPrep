# 2785. Sort Vowels in a String
def sortVowels(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    found = []
    index = []

    for i, char in enumerate(s):
        if char.lower() in vowel: 
            found.append(char)
            index.append(i)


    if len(found) == 0: return s
    s = list(s)
    found = sorted(found)
    for i in range(len(index)):
        s[int(index[i])] = found[i]
    
    return "".join(s)


def findWordsContaining(words, x):
    index = []

    for i, word in enumerate(words):
        if x in word:
            index.append(i)
        

    return index 

    ...


print(findWordsContaining(["leet","code"], "e"))
# 2047. Number of Valid Words in a Sentence ( not solved )
def countValidWords(sentence):
    words = sentence.split() 
    count = 0

    valid = [' ', '-', '!', '.',',']
    valid_words = [".","!"]

    for word in words:
        pass_ = True  
        for char in word:
            if char.isdigit(): pass_ = False 
            elif not char.isalpha() and char not in valid: pass_ = False 

        if pass_ and word[0].isalpha() or word in valid_words:
            count += 1

    return count  
    ...



# print(countValidWords("cat and  dog"))  # 3
# print(countValidWords("!this  1-s b8d!")) # 0
# print(countValidWords("alice and  bob are playing stone-game10")) # 5
# print(countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.")) # 6
# print(countValidWords("pencil-sharpener.")) # 6
print(countValidWords("ab-")) # 0
print(countValidWords("c.,")) # 0
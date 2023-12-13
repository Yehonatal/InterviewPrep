# 2423. Remove Letter To Equalize Frequency
from collections import Counter 
from itertools import count 
def equalFrequency(word):
    # freq = Counter(word)
    # freq_values = list(freq.values())


    # unique_freq = set(freq_values)

    # if len(unique_freq) == 1: return True 
    # elif len(unique_freq) != 1 and 1 or 0 in unique_freq and freq_values.count(1) == 1:
    #     return True 
    # else:
    #     return False 

    ...





print(equalFrequency("abbcc"))
print(equalFrequency("dzwguwwjah"))

print(equalFrequency("ddaccb"))
print(equalFrequency("abcc"))
print(equalFrequency("aazz"))
print(equalFrequency("aaabbbdddffff"))
print(equalFrequency("bac"))

""" from collections import Counter 
def equalFrequency(word):
    works = [] 
    freq = Counter(word)
    freq_values = list(freq.values())

    for i in range(len(freq_values)):
        if len(set(freq_values)) == 1 and list(set(freq_values))[0] == 1:
            return True 
        freq_values[i] -= 1

        if len(set(freq_values)) == 2 and list(set(freq_values))[0] == 0:
            works.append(True)
        elif len(set(freq_values)) != 1:
            works.append(False)
        else:
            works.append(True)

       
        freq_values[i] += 1

    return works 



print(equalFrequency("abbcc"))
print(equalFrequency("dzwguwwjah"))

print(equalFrequency("ddaccb"))
print(equalFrequency("abcc"))
print(equalFrequency("aazz"))
print(equalFrequency("aaabbbdddffff"))
print(equalFrequency("bac"))
 """
    




    # freq = [0] * 26

    # for char in word:
    #     freq[ord(char) - ord("a")] += 1
    
    # return freq

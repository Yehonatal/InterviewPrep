# 2744. Find Maximum Number of String Pairs
def maximumNumberOfStringPairs(words):
    pairs = []
    max_pairs = 0
    
    for word in words:
        pair = {}
        for char in word:
            pair[char] = pair.get(char, 0) + 1

        if pair in pairs:
            max_pairs += 1
        
        pairs.append(pair)
        
    return max_pairs, pairs 


print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
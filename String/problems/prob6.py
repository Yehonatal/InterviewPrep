# 3. Longest Substring Without Repeating Characters ( not solved )
def lengthOfLongestSubstring(s):
    i, j = 0, 0 
    longest = [""]
    seen = [""]

    while j < len(s):
        if s[j] in seen:
            if len(longest[0]) < len(s[i:j]):
                longest.clear()
                longest.append(s[i:j]) 
            i = j
            seen.clear()
        
        
        seen.append(s[j])
        j += 1

    return len(longest[0]) if len(longest[0]) != 0 else len(seen[1])



    ...


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
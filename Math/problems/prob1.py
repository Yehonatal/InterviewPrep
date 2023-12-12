# 1512. Number of Good Pairs
""" 
# 1st Method 
from itertools import combinations
def numIdenticalPairs(nums):
    good = []

    for comb in combinations(nums,2):
        if comb[0] == comb[1]: good.append(comb)


    return len(good) # you can you use a count variable just to increment as well and return 


    # return len([comb for comb in combinations(nums, 2) if comb[0] == comb[1]]) 
"""
def numIdenticalPairs(nums):
    good = 0
    seen = {}

    for num in nums:
        if num in seen:
            good += seen[num]
            seen[num] += 1
        else:
            seen[num] = 1


    return good




print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))
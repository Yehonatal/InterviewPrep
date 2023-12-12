# 1512. Number of Good Pairs
from itertools import combinations 
def numIdenticalPairs(nums):
    pairs = [comb for comb in combinations(nums, 2) if comb[0] == comb[1]]
    return len(pairs)

print(numIdenticalPairs([1,2,3,1,1,3]))
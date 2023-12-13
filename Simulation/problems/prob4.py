# 1920. Build Array from Permutation
from itertools import permutations 
def buildArray(nums):
    # ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

    return [nums[nums[i]] for i in range(len(nums))]

    ans = [0] * len(nums)
    for i in range(len(nums)):
        ans[i] = nums[nums[i]]
        
    return ans



print(buildArray([0,2,1,5,3,4]))
print(buildArray([5,0,1,2,3,4]))
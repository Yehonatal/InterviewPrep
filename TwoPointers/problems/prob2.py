def twoSum(nums, target):
    hash_ = {}

    for i, ele in enumerate(nums):
        comp = target - ele
        if comp in hash_:
            return [hash_[comp], i]

        hash_[ele] = i
    
    return []




print(twoSum([2,7,11,15], 9))
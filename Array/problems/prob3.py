def shuffle(nums, n):
    i, j = 0, n

    shuffled = []

    while j < len(nums):
        shuffled.append(nums[i])
        shuffled.append(nums[j])
        i, j = i + 1, j + 1
    
    return shuffled



print(shuffle([1,2,3,4,4,3,2,1], 4))
print(shuffle([1,1,2,2], 2))
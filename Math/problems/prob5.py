def minimumSum(num):
    nums = sorted([x for x in str(num)])
    pairs = []
    pairs.append(int(str(nums[0]) + str( nums[2])))
    pairs.append(int(str(nums[1]) + str(nums[-1])))

    return sum(pairs)

print(minimumSum(2932))
print(minimumSum(4009))
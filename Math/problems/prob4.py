# 2894. Divisible and Non-divisible Sums Difference
from itertools import count 
def diffOfSums(n, m):
    num1 = 0 # sum of all integers 1, n that are not divisible by m
    num2 = 0 # sum of all integers 1, n that are divisible by m

    nums1 = [num1 + x for x in range(1, n+1) if x % m != 0]
    nums2 = [num2 + x for x in range(1, n+1) if x % m == 0]
    
    return sum(nums1) - sum(nums2)
    # return nums1, nums2

# print(diffOfSums(10, 3))
# print(diffOfSums(5, 6))
print(diffOfSums(5, 1))
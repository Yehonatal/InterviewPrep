def isPalindrome(x):
    if "-" in str(x): return False
    rev = 0
    safe = x
    while x != 0:
        temp = x % 10
        rev = rev * 10 + temp
        x = x // 10

    return rev == safe


    ...


print(isPalindrome(121))
# print(isPalindrome(-121))
# print(isPalindrome(10))
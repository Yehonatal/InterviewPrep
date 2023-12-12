# 2413. Smallest Even Multiple
def smallMul(n):
    return n if n % 2 == 0 else n * 2

print(smallMul(6))
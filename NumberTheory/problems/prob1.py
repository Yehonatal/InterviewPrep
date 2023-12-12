def smallestEvenMultiple(n):    
    return n * 2 if n % 2 != 0 else n
    return n if n % 2 == 0 else n * 2




print(smallestEvenMultiple(5))
print(smallestEvenMultiple(6))
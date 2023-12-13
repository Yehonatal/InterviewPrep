# 1688. Count of Matches in Tournament
def numberOfMatches(n):
    matches = 0

    while n > 1:
        if n % 2 != 0:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
        elif n % 2 == 0:
            matches += n // 2
            n //= 2

    return matches


print(numberOfMatches(7))
print(numberOfMatches(14))
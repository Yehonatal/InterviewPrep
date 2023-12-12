# 2769. Find the Maximum Achievable Number
def theMaximum(num, i):
    x = num + i

    for _ in range(i):
        x += 1

    return x 


print(theMaximum(4,1))
print(theMaximum(3,2))
# 925. Long Pressed Name (not solved )
from collections import Counter 
def isLongPressedName(name, typed):
    name = list(Counter(name).values())
    typed = list(Counter(typed).values())



    result = [0] * len(name)


    for i in range(len(name)):
        result[i] = typed[i] - name[i]
        if result[i] < 0:
            return False 

    return True  

# print(isLongPressedName("alex","aaleex"))
# print(isLongPressedName("saeed","ssaaedd"))

print(isLongPressedName("xnhtq","xhhttqq"))
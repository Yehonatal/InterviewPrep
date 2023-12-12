# 728. Self Dividing Numbers
def selfDividingNum(left, right):
    required = []

    for i in range(left, right+1):
        if '0' in str(i): continue # base to protect zero division

        check = True
        for x in [x for x in str(i)]:
            if i % int(x) != 0: 
                check = False 

        if i not in required and check: 
            required.append(i)
            

    return required
print(selfDividingNum(1, 22))
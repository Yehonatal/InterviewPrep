def this(hours, target):
    return len([hr for hr in hours if hr >= target])

print(this([0,1,2,3,4], 2))
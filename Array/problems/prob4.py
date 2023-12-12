# 2798. Number of Employees Who Met the Target
def this(hours, target):
    return len([hr for hr in hours if hr >= target])

print(this([0,1,2,3,4], 2))
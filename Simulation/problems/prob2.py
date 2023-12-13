# 1389. Create Target Array in the Given Order
def createTargetArray(nums, index):
    output = []
    
    for i in range(len(index)):
        output.insert(index[i], nums[i])

    return output



print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
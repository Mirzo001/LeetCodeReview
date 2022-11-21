nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    newNum = maxTotal = nums[0]    
    for i in range(1, len(nums)):
        newNum = max(nums[i], nums[i] + newNum)
        maxTotal = max(newNum, maxTotal)
    return maxTotal


x=maxSubArray(nums)
print(x)
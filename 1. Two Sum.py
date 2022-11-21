# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [2,7,11,15]
target = 9
# nums = [3,2,4] 
# target = 6

def twoSum(nums, target):
    for index, val in enumerate(nums):
        x = target - val
        
        nums[index] = None
      
        if x in nums:
            return [index, nums.index(x)]

x=twoSum(nums,target)
print(x)


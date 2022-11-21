nums = [0,1,0,3,12]
def moveZeroes(nums):
    # if len(nums) == 0:
    #     return nums
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         nums.append(nums[i])
    #         nums.remove(nums[i])
    # return nums
    
    # good solution though big O(n)
    i = 0
    end = len(nums)
    while i < end:
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            end -= 1
        else:
            i += 1
    return nums
    
    # two line solution 
    # count=nums.count(0)
    # print(count)
    # nums[:]=[i for i in nums if i != 0]
    # nums+=[0]*count
    # return nums
print(moveZeroes(nums))
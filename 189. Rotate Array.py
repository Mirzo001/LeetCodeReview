
nums = [1,2,3,4,5,6,7] 
k = 3

def rotate(nums, k):
        k = k % len(nums)   #take care of the case where k >= len(nums)  
        nums[:] = nums[-k:] + nums[:-k] 
        return nums


# def rotate2(nums, k):
#     for i in range(k):
#         nums[:] = nums.insert(0, nums.pop())
#     print(nums)

x=rotate(nums, k)
print(x)

# def twoSum(nums: List, target):
#         myHash = {}
#         for index, value in enumerate(nums):
#             if target - value in myHash:
#                 print(myHash)
#                 return [myHash[target-value], index]                
#             myHash[value] = index
# print(twoSum(nums=List, target=9))


List = [1,17,11,7,15,2,6]
def twoSum(nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
print(twoSum(nums=List, target=9))
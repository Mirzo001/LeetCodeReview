class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(range(1, len(nums))):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)
#added another solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        return slow+1
#added another solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: left = 0
        left = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[left] = nums[i]
                left += 1
        return left

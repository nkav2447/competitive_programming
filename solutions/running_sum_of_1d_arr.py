class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in range(1, len(nums)):
            nums[num] = nums[num] + nums[num-1]
        return nums

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, ans, curr = 0, len(nums) + 1, 0
        for idx, num in enumerate(nums):
            curr += num
            while curr >= target: ans, left, curr = min(ans, idx - left + 1), left + 1, curr - nums[left]
        return ans < len(nums) + 1 and ans or 0

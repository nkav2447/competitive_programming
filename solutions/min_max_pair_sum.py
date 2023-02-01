class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        nums.sort()
        for i in range(len(nums)/2):
            pair_sum = nums[i] + nums[len(nums)-1-i]
            p = max(p, pair_sum)
        return p

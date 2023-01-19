class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lower_tip, idx_left, res = -1, 0, 0
        for num in nums:
            k -= num % 2
            if nums[idx_left] % 2 == 0:
                idx_left += 1
            if k < 0:
                lower_tip = idx_left
            while k < 0:    
                idx_left += 1
                k += nums[idx_left] % 2
            if k == 0:
                res += idx_left - lower_tip
        return res

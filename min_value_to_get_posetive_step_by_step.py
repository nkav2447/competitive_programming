class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        min_val = min(nums)
        if min_val < 0:
            return abs(min_val) + 1
        else:
            return 1

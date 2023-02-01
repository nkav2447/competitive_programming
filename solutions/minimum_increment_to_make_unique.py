class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aggregate = 0
        nums.sort()
        for num in range(1, len(nums)):
            if nums[num] <= nums[num-1]:
                val = nums[num-1]+1
                aggregate += val - nums[num]
                nums[num] = val
        return aggregate

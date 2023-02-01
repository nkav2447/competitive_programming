class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        permutation, left = False, len(nums) - 2
        while 0 <= left:
            right = len(nums) - 1  
            while left < right and nums[right] <= nums[left]: 
                right -= 1
            if right <= left: 
                left -= 1
            else:
                nums[left], nums[left + 1:], permutation = nums[right], sorted(nums[left + 1:right] + [nums[left]] + nums[right + 1:]), True
                break
        if not permutation: nums.sort()

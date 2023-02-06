#added another solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != 0:
                slow += 1
                fast += 1
            elif nums[fast] == 0 :
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
#added another solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, items = 0, 0
        while i<len(nums) and items<=len(nums):
            if nums[i] == 0: 
                nums.append(0)
                nums.pop(i) 
                i-=1
            i+=1 
            items+=1

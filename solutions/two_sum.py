#another solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}  
        for i, num in enumerate(nums):
            if target - num in num_idx:
                return [num_idx[target - num], i]
            else:
                num_idx[num] = i
#another solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            compt = target - nums[i]
            if not compt in dic:
                dic[nums[i]] = i
            else:
                return [dic[compt], i]

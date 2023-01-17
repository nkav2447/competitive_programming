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

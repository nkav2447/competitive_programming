class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        res = []
        [res.append(i) for i, x in enumerate(nums) if x == target]
        return res

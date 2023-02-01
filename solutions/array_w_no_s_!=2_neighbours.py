class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        res = [-1]*len(nums)
        mid_index = len(nums) // 2
        mid_num = nums_sorted[mid_index]
        for i in range(1, len(nums), 2):
            if nums_sorted[0] < mid_num:
                p = nums_sorted.pop(0)
                res[i] = p
        for i in range(0, len(nums), 2):
            if len(nums_sorted):
                p = nums_sorted.pop(0)
                res[i] = p
        return res

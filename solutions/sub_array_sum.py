class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ctr = 0
        tally = 0
        prefix_sum = {0 : 1}
        for num in nums:
            tally += num
            diff = tally - k
            ctr += prefix_sum.get(diff, 0)
            prefix_sum[tally] = 1 + prefix_sum.get(tally, 0)
        return ctr

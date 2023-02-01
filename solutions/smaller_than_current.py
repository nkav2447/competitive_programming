class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return list(map(lambda n: sorted(nums).index(n), nums))

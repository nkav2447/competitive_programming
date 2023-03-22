#another solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            current = [x for x in nums if x < num]
            res.append(len(current))
        return res
#another solution
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return list(map(lambda n: sorted(nums).index(n), nums))
    


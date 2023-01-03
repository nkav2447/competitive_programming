class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        ans = 0
        for k,v in dic.items():
            if(len(v) >= 2):
                m = len(v)
                ans += m*(m-1)/2
        return int(ans)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import nlargest
        hashmap = {}
        for elt in nums:
            if elt in hashmap:
                hashmap[elt] += 1
            else:
                hashmap[elt] = 1
        return nlargest(k, hashmap.keys(), key=hashmap.get)

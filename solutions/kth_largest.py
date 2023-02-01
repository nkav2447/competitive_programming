from heapq import heapify, heappop
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        max_heap = [-int(n) for n in nums]
        heapify(max_heap)
        while k > 1:
            heappop(max_heap)
            k -= 1
        return str(-max_heap[0])

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        from heapq import heappop, heappush
        heap, res, j = [], [], 0
        while head:
            res.append(0)
            while heap and heap[0][0] < head.val:
                val, i = heappop(heap)
                res[i] = head.val
            heappush(heap, (head.val, j))
            j += 1
            head = head.next
        return res

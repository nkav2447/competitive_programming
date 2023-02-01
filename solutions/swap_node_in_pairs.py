# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head
        curr = head.next
        next = head
        next.next = self.swapPairs(curr.next)
        curr.next = next
        return curr

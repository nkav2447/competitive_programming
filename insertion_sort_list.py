# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ref, ref.next, n = ListNode(-5000), head, 0
        while head:
            inserted, curr, prev, n = ListNode(head.val), ref.next, ref, n+1
            for i in range(n-1):
                if inserted.val<curr.val:
                    prev.next, inserted.next = inserted, curr
                    if i >= n-2: curr.next = None
                    break
                else: 
                    prev, curr = curr, curr.next
                if i == n-2: prev.next = inserted 
            head = head.next
        return ref.next

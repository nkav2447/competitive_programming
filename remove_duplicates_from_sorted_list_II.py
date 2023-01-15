# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_left, dummy_left.next = ListNode(-1), head
        prev, prev_num = None, dummy_left
        while head:
            if prev is not None and prev.val != head.val: 
                prev_num = prev
            if prev is not None and prev.val == head.val:
                while head and head.next and head.next.val == head.val: 
                    head = head.next
                head = head.next
                prev_num.next = head
            prev = head
            if head is not None: 
                head = head.next
        return dummy_left.next

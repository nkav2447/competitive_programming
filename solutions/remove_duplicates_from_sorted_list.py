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
        temp = root = head
        while head:
            if head.val != temp.val:
                temp.next = temp = head
            head = temp.next = head.next
        return root

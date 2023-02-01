# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        right = fast = head
        left = None
        while fast and fast.next:
            fast = fast.next.next
            right.next, left, right = left, right, right.next
        if fast: right = right.next
        while left and right and left.val == right.val:
            left, right = left.next, right.next
        return not left

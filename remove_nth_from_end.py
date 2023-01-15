# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        array = [temp]
        while head is not None:
            array.append(head)
            head = head.next
        for _ in range(n + 1):
            pre = array.pop()
        pre.next = pre.next.next
        return temp.next

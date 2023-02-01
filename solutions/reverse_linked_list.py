# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        elif head != None and head.next == None:
            return head
        else:
            temp = None
            nxt_node = None
            while head:
                nxt_node = head.next
                head.next = temp
                temp = head
                head = nxt_node
        return temp

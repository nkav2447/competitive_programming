# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_most_depth = self.maxDepth(root.left)
        right_most_depth = self.maxDepth(root.right)
        return max(left_most_depth, right_most_depth) + 1

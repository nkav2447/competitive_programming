class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def depth_fs(left, right, player1, player2, curr_turn):
            if left > right:
                return player1 >= player2
            elif curr_turn:
                return depth_fs(left + 1, right, player1 + nums[left], player2, 0) or depth_fs(left, right - 1, player1 + nums[right], player2, 0)
            else:
                return depth_fs(left + 1, right, player1, player2 + nums[left], 1) and depth_fs(left, right - 1, player1, player2 + nums[right], 1)
        return depth_fs(0, len(nums) - 1, 0, 0, 1)

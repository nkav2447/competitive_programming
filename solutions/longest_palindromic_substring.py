class Solution:
    def helper(self,left, right, s):
        while left >= 0 and right < len(s):
            if s[left] != s[right]: 
                break
            left -= 1
            right += 1
        return [left+1, right]
    def longestPalindrome(self, s: str) -> str:
        bef_max = [0,1]
        for i in range(len(s)):
            even = self.helper(i-1,i,s)
            odd = self.helper(i-1, i+1, s)
            if odd[1]-odd[0] > even[1]-even[0]:
                curr_max = odd
            else:
                curr_max = even
            if bef_max[1]-bef_max[0] > curr_max[1] - curr_max[0]:
                bef_max = bef_max
            else:
                bef_max = curr_max
        return s[bef_max[0]:bef_max[1]]

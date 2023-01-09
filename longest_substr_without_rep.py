class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        collection = set()
        left , res = 0, 0
        for right in range(len(s)):
            while s[right] in collection:
                collection.remove(s[left])
                left += 1
            collection.add(s[right])
            res = max(res, right - left + 1)
        return res

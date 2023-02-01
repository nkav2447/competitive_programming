class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        i, j, maximum = 0, 0, 0
        chr_set = set()
        while i < len(s):
            while s[i] in chr_set:
                chr_set.remove(s[j])
                j += 1
            chr_set.add(s[i])
            maximum = max(maximum, i-j+1)
            i += 1
        return maximum

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
